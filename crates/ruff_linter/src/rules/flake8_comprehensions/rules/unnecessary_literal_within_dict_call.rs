use std::fmt;

use ruff_python_ast::{self as ast, Expr};

use ruff_macros::{ViolationMetadata, derive_message_formats};
use ruff_text_size::Ranged;

use crate::checkers::ast::Checker;
use crate::{AlwaysFixableViolation, Edit, Fix};

use crate::rules::flake8_comprehensions::helpers;

/// ## What it does
/// Checks for `dict()` calls that take unnecessary dict literals or dict
/// comprehensions as arguments.
///
/// ## Why is this bad?
/// It's unnecessary to wrap a dict literal or comprehension within a `dict()`
/// call, since the literal or comprehension syntax already returns a
/// dictionary.
///
/// ## Example
/// ```python
/// dict({})
/// dict({"a": 1})
/// ```
///
/// Use instead:
/// ```python
/// {}
/// {"a": 1}
/// ```
///
/// ## Fix safety
/// This rule's fix is marked as unsafe, as it may occasionally drop comments
/// when rewriting the call. In most cases, though, comments will be preserved.
#[derive(ViolationMetadata)]
pub(crate) struct UnnecessaryLiteralWithinDictCall {
    kind: DictKind,
}

impl AlwaysFixableViolation for UnnecessaryLiteralWithinDictCall {
    #[derive_message_formats]
    fn message(&self) -> String {
        let UnnecessaryLiteralWithinDictCall { kind } = self;
        format!("Unnecessary dict {kind} passed to `dict()` (remove the outer call to `dict()`)")
    }

    fn fix_title(&self) -> String {
        "Remove outer `dict()` call".to_string()
    }
}

/// C418
pub(crate) fn unnecessary_literal_within_dict_call(checker: &Checker, call: &ast::ExprCall) {
    if !call.arguments.keywords.is_empty() {
        return;
    }
    if call.arguments.args.len() > 1 {
        return;
    }
    let Some(argument) =
        helpers::first_argument_with_matching_function("dict", &call.func, &call.arguments.args)
    else {
        return;
    };
    let Some(argument_kind) = DictKind::try_from_expr(argument) else {
        return;
    };
    if !checker.semantic().has_builtin_binding("dict") {
        return;
    }

    let mut diagnostic = checker.report_diagnostic(
        UnnecessaryLiteralWithinDictCall {
            kind: argument_kind,
        },
        call.range(),
    );

    // Convert `dict({"a": 1})` to `{"a": 1}`
    diagnostic.set_fix({
        // Delete from the start of the call to the start of the argument.
        let call_start = Edit::deletion(call.start(), argument.start());

        // Delete from the end of the argument to the end of the call.
        let call_end = Edit::deletion(argument.end(), call.end());

        Fix::unsafe_edits(call_start, [call_end])
    });
}

#[derive(Debug, Copy, Clone, PartialEq, Eq)]
pub(crate) enum DictKind {
    Literal,
    Comprehension,
}

impl DictKind {
    const fn as_str(self) -> &'static str {
        match self {
            Self::Literal => "literal",
            Self::Comprehension => "comprehension",
        }
    }

    const fn try_from_expr(expr: &Expr) -> Option<Self> {
        match expr {
            Expr::Dict(_) => Some(Self::Literal),
            Expr::DictComp(_) => Some(Self::Comprehension),
            _ => None,
        }
    }
}

impl fmt::Display for DictKind {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        f.write_str(self.as_str())
    }
}
