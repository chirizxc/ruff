use ruff_macros::{ViolationMetadata, derive_message_formats};
use ruff_python_ast::{self as ast};
use ruff_text_size::Ranged;

use crate::Violation;
use crate::checkers::ast::Checker;

/// ## What it does
/// Checks for uses of the SNMPv3 protocol without encryption.
///
/// ## Why is this bad?
/// Unencrypted SNMPv3 communication can be intercepted and read by
/// unauthorized parties. Instead, enable encryption when using SNMPv3.
///
/// ## Example
/// ```python
/// from pysnmp.hlapi import UsmUserData
///
/// UsmUserData("user")
/// ```
///
/// Use instead:
/// ```python
/// from pysnmp.hlapi import UsmUserData
///
/// UsmUserData("user", "authkey", "privkey")
/// ```
///
/// ## References
/// - [Common Weakness Enumeration: CWE-319](https://cwe.mitre.org/data/definitions/319.html)
#[derive(ViolationMetadata)]
pub(crate) struct SnmpWeakCryptography;

impl Violation for SnmpWeakCryptography {
    #[derive_message_formats]
    fn message(&self) -> String {
        "You should not use SNMPv3 without encryption. `noAuthNoPriv` & `authNoPriv` is insecure."
            .to_string()
    }
}

/// S509
pub(crate) fn snmp_weak_cryptography(checker: &Checker, call: &ast::ExprCall) {
    if call.arguments.len() < 3 {
        if checker
            .semantic()
            .resolve_qualified_name(&call.func)
            .is_some_and(|qualified_name| {
                matches!(
                    qualified_name.segments(),
                    ["pysnmp", "hlapi", "UsmUserData"]
                )
            })
        {
            checker.report_diagnostic(SnmpWeakCryptography, call.func.range());
        }
    }
}
