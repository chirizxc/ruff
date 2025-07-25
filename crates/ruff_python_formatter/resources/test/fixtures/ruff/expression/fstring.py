(
    f'{one}'
    f'{two}'
)


rf"Not-so-tricky \"quote"

# Regression test for fstrings dropping comments
result_f = (
    'Traceback (most recent call last):\n'
    f'  File "{__file__}", line {lineno_f+5}, in _check_recursive_traceback_display\n'
    '    f()\n'
    f'  File "{__file__}", line {lineno_f+1}, in f\n'
    '    f()\n'
    f'  File "{__file__}", line {lineno_f+1}, in f\n'
    '    f()\n'
    f'  File "{__file__}", line {lineno_f+1}, in f\n'
    '    f()\n'
    # XXX: The following line changes depending on whether the tests
    # are run through the interactive interpreter or with -m
    # It also varies depending on the platform (stack size)
    # Fortunately, we don't care about exactness here, so we use regex
    r'  \[Previous line repeated (\d+) more times\]' '\n'
    'RecursionError: maximum recursion depth exceeded\n'
)


# Regression for fstring dropping comments that were accidentally attached to
# an expression inside a formatted value
(
    f'{1}'
    # comment 1
    ''
)

(
    f'{1}'  # comment 2
    f'{2}'
)

(
    f'{1}'
    f'{2}'  # comment 3
)

(
    1, (  # comment 4
        f'{2}'
    )
)

(
    (
        f'{1}'
        # comment 5
    ),
    2
)

# https://github.com/astral-sh/ruff/issues/6841
x = f'''a{""}b'''
y = f'''c{1}d"""e'''
z = f'''a{""}b''' f'''c{1}d"""e'''

# F-String formatting test cases (Preview)

# Simple expression with a mix of debug expression and comments.
x = f"{a}"
x = f"{
    a = }"
x = f"{ # comment 6
    a }"
x = f"{   # comment 7
    a = }"

# Remove the parentheses as adding them doesn't make then fit within the line length limit.
# This is similar to how we format it before f-string formatting.
aaaaaaaaaaa = (
    f"asaaaaaaaaaaaaaaaa { aaaaaaaaaaaa + bbbbbbbbbbbb + ccccccccccccccc + dddddddd } cccccccccc"
)
# Here, we would use the best fit layout to put the f-string indented on the next line
# similar to the next example.
aaaaaaaaaaa = f"asaaaaaaaaaaaaaaaa { aaaaaaaaaaaa + bbbbbbbbbbbb + ccccccccccccccc } cccccccccc"
aaaaaaaaaaa = (
    f"asaaaaaaaaaaaaaaaa { aaaaaaaaaaaa + bbbbbbbbbbbb + ccccccccccccccc } cccccccccc"
)

# This should never add the optional parentheses because even after adding them, the
# f-string exceeds the line length limit.
x = f"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa { "bbbbbbbbbbbbbbbbbbbbbbbbbbbbb" } ccccccccccccccc"
x = f"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa { "bbbbbbbbbbbbbbbbbbbbbbbbbbbbb" = } ccccccccccccccc"
x = f"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa { # comment 8
                                             "bbbbbbbbbbbbbbbbbbbbbbbbbbbbb" } ccccccccccccccc"
x = f"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa { # comment 9
                                             "bbbbbbbbbbbbbbbbbbbbbbbbbbbbb" = } ccccccccccccccc"
x = f"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa { # comment 9
                                             'bbbbbbbbbbbbbbbbbbbbbbbbbbbbb' = } ccccccccccccccc"

# Multiple larger expressions which exceeds the line length limit. Here, we need to decide
# whether to split at the first or second expression. This should work similarly to the
# assignment statement formatting where we split from right to left in preview mode.
x = f"aaaaaaaaaaaa { bbbbbbbbbbbbbb } cccccccccccccccccccc { ddddddddddddddd } eeeeeeeeeeeeee"

# The above example won't split but when we start introducing line breaks:
x = f"aaaaaaaaaaaa {
        bbbbbbbbbbbbbb } cccccccccccccccccccc { ddddddddddddddd } eeeeeeeeeeeeee"
x = f"aaaaaaaaaaaa { bbbbbbbbbbbbbb
                    } cccccccccccccccccccc { ddddddddddddddd } eeeeeeeeeeeeee"
x = f"aaaaaaaaaaaa { bbbbbbbbbbbbbb } cccccccccccccccccccc {
        ddddddddddddddd } eeeeeeeeeeeeee"
x = f"aaaaaaaaaaaa { bbbbbbbbbbbbbb } cccccccccccccccccccc { ddddddddddddddd
                                                            } eeeeeeeeeeeeee"

# But, in case comments are present, we would split at the expression containing the
# comments:
x = f"aaaaaaaaaaaa { bbbbbbbbbbbbbb # comment 10
                    } cccccccccccccccccccc { ddddddddddddddd } eeeeeeeeeeeeee"
x = f"aaaaaaaaaaaa { bbbbbbbbbbbbbb
                    } cccccccccccccccccccc { # comment 11
                                            ddddddddddddddd } eeeeeeeeeeeeee"

# Here, the expression part itself starts with a curly brace so we need to add an extra
# space between the opening curly brace and the expression.
x = f"{ {'x': 1, 'y': 2} }"
# Although the extra space isn't required before the ending curly brace, we add it for
# consistency.
x = f"{ {'x': 1, 'y': 2}}"
x = f"{ {'x': 1, 'y': 2} = }"
x = f"{  # comment 12
    {'x': 1, 'y': 2} }"
x = f"{    # comment 13
    {'x': 1, 'y': 2} = }"
# But, if there's a format specifier or a conversion flag then we don't need to add
# any whitespace at the end
x = f"aaaaa { {'aaaaaa', 'bbbbbbb', 'ccccccccc'}!s} bbbbbb"
x = f"aaaaa { {'aaaaaa', 'bbbbbbb', 'ccccccccc'}:.3f} bbbbbb"

# But, in this case, we would split the expression itself because it exceeds the line
# length limit so we need not add the extra space.
xxxxxxx = f"{
    {'aaaaaaaaaaaaaaaaaaa', 'bbbbbbbbbbbbbbbbbbbbbb', 'ccccccccccccccccccccc'}
}"
# And, split the expression itself because it exceeds the line length.
xxxxxxx = f"{
    {'aaaaaaaaaaaaaaaaaaaaaaaaa', 'bbbbbbbbbbbbbbbbbbbbbbbbbbb', 'cccccccccccccccccccccccccc'}
}"

#############################################################################################
# Quotes
#############################################################################################
f"foo 'bar' {x}"
f"foo \"bar\" {x}"
f'foo "bar" {x}'
f'foo \'bar\' {x}'
f"foo {"bar"}"

f"single quoted '{x}' double quoted \"{x}\"" # Same number of quotes => use preferred quote style
f"single quote ' {x} double quoted \"{x}\""  # More double quotes => use single quotes
f"single quoted '{x}' double quote \" {x}"  # More single quotes => use double quotes

fr"single quotes ' {x}"  # Keep double because `'` can't be escaped
fr'double quotes " {x}'  # Keep single because `"` can't be escaped
fr'flip quotes {x}'  # Use preferred quotes, because raw string contains now quotes.

# Here, the formatter will remove the escapes which is correct because they aren't allowed
# pre 3.12. This means we can assume that the f-string is used in the context of 3.12.
f"foo {'\'bar\''}"
f"foo {'\"bar\"'}"

# Quotes inside the expressions have no impact on the quote selection of the outer string.
# Required so that the following two examples result in the same formatting.
f'foo {10 + len("bar")}'
f"foo {10 + len('bar')}"

# Pre 312, preserve the outer quotes if the f-string contains quotes in the debug expression
f'foo {10 + len("bar")=}'
f'''foo {10 + len('''bar''')=}'''
f'''foo {10 + len('bar')=}'''  # Fine to change the quotes because it uses triple quotes

# Triple-quoted strings
# It's ok to use the same quote char for the inner string if it's single-quoted.
f"""test {'inner'}"""
f"""test {"inner"}"""
# But if the inner string is also triple-quoted then we should preserve the existing quotes.
f"""test {'''inner'''}"""

# It's not okay to change the quote style if the inner string is triple quoted and contains a quote.
f'{"""other " """}'
f'{"""other " """ + "more"}'
f'{b"""other " """}'
f'{f"""other " """}'

# Not valid Pre 3.12
f"""test {f'inner {'''inner inner'''}'}"""
f"""test {f'''inner {"""inner inner"""}'''}"""

# Magic trailing comma
#
# The expression formatting will result in breaking it across multiple lines with a
# trailing comma but as the expression isn't already broken, we will remove all the line
# breaks which results in the trailing comma being present. This test case makes sure
# that the trailing comma is removed as well.
f"aaaaaaa {['aaaaaaaaaaaaaaa', 'bbbbbbbbbbbbb', 'ccccccccccccccccc', 'ddddddddddddddd', 'eeeeeeeeeeeeee']} aaaaaaa"

# And, if the trailing comma is already present, we still need to remove it.
f"aaaaaaa {['aaaaaaaaaaaaaaa', 'bbbbbbbbbbbbb', 'ccccccccccccccccc', 'ddddddddddddddd', 'eeeeeeeeeeeeee',]} aaaaaaa"

# Keep this Multiline by breaking it at the square brackets.
f"""aaaaaa {[
    xxxxxxxx,
    yyyyyyyy,
]} ccc"""

# Add the magic trailing comma because the elements don't fit within the line length limit
# when collapsed.
f"aaaaaa {[
    xxxxxxxxxxxx,
    xxxxxxxxxxxx,
    xxxxxxxxxxxx,
    xxxxxxxxxxxx,
    xxxxxxxxxxxx,
    xxxxxxxxxxxx,
    yyyyyyyyyyyy
]} ccccccc"

# Remove the parentheses because they aren't required
xxxxxxxxxxxxxxx = (
    f"aaaaaaaaaaaaaaaa bbbbbbbbbbbbbbb {
        xxxxxxxxxxx  # comment 14
        + yyyyyyyyyy
    } dddddddddd"
)

# Comments

# No comments should be dropped!
f"{ # comment 15
    # comment 16
    foo # comment 17
    # comment 18
}"  # comment 19
# comment 20

# The specifier of an f-string must hug the closing `}` because a multiline format specifier is invalid syntax in a single
# quoted f-string.
f"aaaaaaaaaaaaaaaa bbbbbbbbbbbbbbbbbb ccccccccccc {variable
:.3f} ddddddddddddddd eeeeeeee"

# The same applies for triple quoted f-strings, except that we need to preserve the newline before the closing `}`.
# or we risk altering the meaning of the f-string.
f"""aaaaaaaaaaaaaaaa bbbbbbbbbbbbbbbbbb ccccccccccc {variable
    :.3f} ddddddddddddddd eeeeeeee"""
f"""aaaaaaaaaaaaaaaa bbbbbbbbbbbbbbbbbb ccccccccccc {variable:.3f
} ddddddddddddddd eeeeeeee"""

aaaaaaaaaaa = f"""asaaaaaaaaaaaaaaaa {
   aaaaaaaaaaaa + bbbbbbbbbbbb + ccccccccccccccc + dddddddd
   # comment
   :.3f} cccccccccc"""

# Throw in a random comment in it but surprise, this is not a comment but just a text
# which is part of the format specifier
aaaaaaaaaaa = f"""asaaaaaaaaaaaaaaaa {
        aaaaaaaaaaaa + bbbbbbbbbbbb + ccccccccccccccc + dddddddd:.3f
     # comment
} cccccccccc"""
aaaaaaaaaaa = f"""asaaaaaaaaaaaaaaaa {
        aaaaaaaaaaaa + bbbbbbbbbbbb + ccccccccccccccc + dddddddd:.3f
     # comment} cccccccccc"""

# Conversion flags
#

# Even in the case of debug expressions, we only need to preserve the whitespace within
# the expression part of the replacement field.
x = f"aaaaaaaaa { x   = !r  }"

# Combine conversion flags with format specifiers
x = f"{x   =   !s
         :>0}"

x = f"{
    x!s:>{
        0
        # comment 21-2
    }}"

f"{1
    # comment 21-3
:}"

f"{1 # comment 21-4
:} a"


x = f"""
{              # comment 22
 x =   :.0{y # comment 23
           }f}"""

# Here, the debug expression is in a nested f-string so we should start preserving
# whitespaces from that point onwards. This means we should format the outer f-string.
x = f"""{"foo " +    # comment 24
    f"{   x =

       }"    # comment 25
 }
        """

# Mix of various features.
f"""{  # comment 26
    foo # after foo
   :>{
          x # after x
          }
    # comment 27
    # comment 28
} woah {x}"""


f"""{foo
      :a{
      a # comment 29
      # comment 30
      }
}"""

# Regression test for https://github.com/astral-sh/ruff/issues/18672
f"{
    # comment 31
    foo
   :>}"

# Assignment statement

# Even though this f-string has multiline expression, thus allowing us to break it at the
# curly braces, the f-string fits on a single line if it's moved inside the parentheses.
# We should prefer doing that instead.
aaaaaaaaaaaaaaaaaa = f"testeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee{
    expression}moreeeeeeeeeeeeeeeee"

# Same as above
xxxxxxx = f"{
    {'aaaaaaaaaaaaaaaaaaa', 'bbbbbbbbbbbbbbbbbbb', 'cccccccccccccccccccccccccc'}
}"

# Similar to the previous example, but the f-string will exceed the line length limit,
# we shouldn't add any parentheses here.
xxxxxxx = f"{
    {'aaaaaaaaaaaaaaaaaaaaaaaaa', 'bbbbbbbbbbbbbbbbbbbbbbbbbbb', 'cccccccccccccccccccccccccc'}
}"

# Same as above but with an inline comment. The f-string should be formatted inside the
# parentheses and the comment should be part of the line inside the parentheses.
aaaaaaaaaaaaaaaaaa = f"testeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee{
    expression}moreeeeeeeeeeeeeeeee"  # comment

# Similar to the previous example but this time parenthesizing doesn't work because it
# exceeds the line length. So, avoid parenthesizing this f-string.
aaaaaaaaaaaaaaaaaa = f"testeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee{
    expression}moreeeeeeeeeeeeeeeee"  # comment loooooooong

# Similar to the previous example but we start with the parenthesized layout. This should
# remove the parentheses and format the f-string on a single line. This shows that the
# final layout for the formatter is same for this and the previous case. The only
# difference is that in the previous case the expression is already mulitline which means
# the formatter can break it further at the curly braces.
aaaaaaaaaaaaaaaaaa = (
    f"testeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee{expression}moreeeeeeeeeeeeeeeee"  # comment loooooooong
)

# The following f-strings are going to break because of the trailing comma so we should
# avoid using the best fit layout and instead use the default layout.
# left-to-right
aaaa = f"aaaa {[
    1, 2,
]} bbbb"
# right-to-left
aaaa, bbbb = f"aaaa {[
    1, 2,
]} bbbb"

# Using the right-to-left assignment statement variant.
aaaaaaaaaaaaaaaaaa, bbbbbbbbbbb = f"testeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee{
    expression}moreeeeeeeeeeeeeeeee"  # comment

# Here, the f-string layout is flat but it exceeds the line length limit. This shouldn't
# try the custom best fit layout because the f-string doesn't have any split points.
aaaaaaaaaaaa["bbbbbbbbbbbbbbbb"] = (
    f"aaaaaaaaaaaaaaaaaaa {aaaaaaaaa + bbbbbbbbbbb + cccccccccccccc} ddddddddddddddddddd"
)
# Same as above but without the parentheses to test that it gets formatted to the same
# layout as the previous example.
aaaaaaaaaaaa["bbbbbbbbbbbbbbbb"] = f"aaaaaaaaaaaaaaaaaaa {aaaaaaaaa + bbbbbbbbbbb + cccccccccccccc} ddddddddddddddddddd"

# But, the following f-string does have a split point because of the multiline expression.
aaaaaaaaaaaa["bbbbbbbbbbbbbbbb"] = (
    f"aaaaaaaaaaaaaaaaaaa {
        aaaaaaaaa + bbbbbbbbbbb + cccccccccccccc} ddddddddddddddddddd"
)
aaaaaaaaaaaa["bbbbbbbbbbbbbbbb"] = (
    f"aaaaaaaaaaaaaaaaaaa {
        aaaaaaaaaaaaaaaaaaaa + bbbbbbbbbbbbbbbbbbbbb + cccccccccccccccccccccc + dddddddddddddddddddddddddddd} ddddddddddddddddddd"
)

# This is an implicitly concatenated f-string but it cannot be joined because otherwise
# it'll exceed the line length limit. So, the two f-strings will be inside parentheses
# instead and the inline comment should be outside the parentheses.
a = f"test{
    expression
}flat" f"can be {
    joined
} togethereeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee" # inline

# Similar to the above example but this fits within the line length limit.
a = f"test{
    expression
}flat" f"can be {
    joined
} togethereeeeeeeeeeeeeeeeeeeeeeeeeee" # inline

# The following test cases are adopted from implicit string concatenation but for a
# single f-string instead.

# Don't inline f-strings that contain expressions that are guaranteed to split, e.g. because of a magic trailing comma
aaaaaaaaaaaaaaaaaa = f"testeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee{
[a,]
}moreeeeeeeeeeeeeeeeeeee" # comment

aaaaaaaaaaaaaaaaaa = (
    f"testeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee{
[a,]
}moreeeeeeeeeeeeeeeeeeee" # comment
)

aaaaa[aaaaaaaaaaa] = f"testeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee{
[a,]
}moreeeeeeeeeeeeeeeeeeee" # comment

aaaaa[aaaaaaaaaaa] = (f"testeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee{
[a,]
}moreeeeeeeeeeeeeeeeeeee" # comment
)

# Don't inline f-strings that contain commented expressions
aaaaaaaaaaaaaaaaaa = (
    f"testeeeeeeeeeeeeeeeeeeeeeeeee{[
        a  # comment
    ]}moreeeeeeeeeeeeeeeeeetest"  # comment
)

aaaaa[aaaaaaaaaaa] = (
    f"testeeeeeeeeeeeeeeeeeeeeeeeee{[
        a  # comment
    ]}moreeeeeeeeeeeeeeeeeetest"  # comment
)

# Don't inline f-strings with multiline debug expressions or format specifiers
aaaaaaaaaaaaaaaaaa = (
    f"testeeeeeeeeeeeeeeeeeeeeeeeee{
    a=}moreeeeeeeeeeeeeeeeeetest"  # comment
)

aaaaaaaaaaaaaaaaaa = (
    f"testeeeeeeeeeeeeeeeeeeeeeeeee{a +
    b=}moreeeeeeeeeeeeeeeeeetest"  # comment
)

aaaaaaaaaaaaaaaaaa = (
    f"testeeeeeeeeeeeeeeeeeeeeeeeee{a
    =}moreeeeeeeeeeeeeeeeeetest"  # comment
)

aaaaa[aaaaaaaaaaa] = (
    f"testeeeeeeeeeeeeeeeeeeeeeeeee{
    a=}moreeeeeeeeeeeeeeeeeetest"  # comment
)

aaaaa[aaaaaaaaaaa] = (
    f"testeeeeeeeeeeeeeeeeeeeeeeeee{a
    =}moreeeeeeeeeeeeeeeeeetest"  # comment
)

# This is not a multiline f-string even though it has a newline after the format specifier.
aaaaaaaaaaaaaaaaaa = f"testeeeeeeeeeeeeeeeeeeeeeeeee{
    a:.3f}moreeeeeeeeeeeeeeeeeetest"  # comment

aaaaaaaaaaaaaaaaaa = (
    f"testeeeeeeeeeeeeeeeeeeeeeeeee{
    a:.3f}moreeeeeeeeeeeeeeeeeetest"  # comment
)

# The newline is only considered when it's a tripled-quoted f-string.
aaaaaaaaaaaaaaaaaa = f"""testeeeeeeeeeeeeeeeeeeeeeeeee{
    a:.3f
    }moreeeeeeeeeeeeeeeeeetest"""  # comment

aaaaaaaaaaaaaaaaaa = (
    f"""testeeeeeeeeeeeeeeeeeeeeeeeee{
    a:.3f
    }moreeeeeeeeeeeeeeeeeetest"""  # comment
)

# Remove the parentheses here
aaaaaaaaaaaaaaaaaa = (
    f"testeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee{[a, b,
    # comment
    ]}moee" # comment
)
# ... but not here because of the ownline comment
aaaaaaaaaaaaaaaaaa = (
    f"testeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee{[a, b,
    ]}moee"
    # comment
)

# F-strings in other positions

if f"aaaaaaaaaaa {ttttteeeeeeeeest} more {
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
}": pass

if (
    f"aaaaaaaaaaa {ttttteeeeeeeeest} more {
        aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    }"
): pass

if f"aaaaaaaaaaa {ttttteeeeeeeeest} more {
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
}": pass

if f"aaaaaaaaaaa {ttttteeeeeeeeest} more {  # comment
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
}": pass

if f"aaaaaaaaaaa {[ttttteeeeeeeeest,]} more {
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
}":
    pass

if (
    f"aaaaaaaaaaa {[ttttteeeeeeeeest,]} more {
        aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    }"
):
    pass

if f"aaaaaaaaaaa {[ttttteeeeeeeeest,]} more {
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
}":
    pass

# For loops
for a in f"testeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee{
        expression}moreeeeeeeeeeeeeeeeeeee":
    pass

for a in f"testeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee{expression}moreeeeeeeeeeeeeeeeeeeeeeeeeeeeee":
    pass

for a in f"testeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee{
        expression}moreeeeeeeeeeeeeeeeeeeeeeeeeeeeee":
    pass

for a in (
    f"testeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee{expression}moreeeeeeeeeeeeeeeeeeeeeeeeeeeee"
):
    pass

# With statements
with f"testeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee{
        expression}moreeeeeeeeeeeeeeeeeeee":
    pass

with f"testeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee{expression}moreeeeeeeeeeeeeeeeeeeeeeeeeeeeee":
    pass

with f"testeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee{
        expression}moreeeeeeeeeeeeeeeeeeeeeeeeeeeeee":
    pass

with (
    f"testeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee{expression}moreeeeeeeeeeeeeeeeeeeeeeeeeeeee"
):
    pass

# Assert statements
assert f"aaaaaaaaa{
        expression}bbbbbbbbbbbb", f"cccccccccc{
                expression}dddddddddd"

assert f"aaaaaaaaa{expression}bbbbbbbbbbbb", f"cccccccccccccccc{
        expression}dddddddddddddddd"

assert f"aaaaaaaaa{expression}bbbbbbbbbbbb", f"cccccccccccccccc{expression}dddddddddddddddd"

assert f"aaaaaaaaaaaaaaaaaaaaaaaaaaa{
        expression}bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb", f"ccccccc{expression}dddddddddd"

assert f"aaaaaaaaaaaaaaaaaaaaaaaaaaa{expression}bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb", f"ccccccc{expression}dddddddddd"

assert f"aaaaaaaaaaaaaaaaaaaaaaaaaaa{
        expression}bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb", f"ccccccccccccccccccccc {
                expression} dddddddddddddddddddddddddd"

assert f"aaaaaaaaaaaaaaaaaaaaaaaaaaa{expression}bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb", f"cccccccccccccccccccccccccccccccc {expression} ddddddddddddddddddddddddddddddddddddd"

# F-strings as a single argument to a call expression to test whether it's huggable or not.
call(f"{
    testeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
}")

call(f"{
    testeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
}")

call(f"{  # comment
    testeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
}")

call(f"""aaaaaaaaaaaaaaaa bbbbbbbbbb {testeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee}""")

call(f"""aaaaaaaaaaaaaaaa bbbbbbbbbb {testeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                }""")

call(f"""aaaaaaaaaaaaaaaa
     bbbbbbbbbb {testeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
                }""")

call(f"""aaaaaaaaaaaaaaaa
     bbbbbbbbbb {testeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee  # comment
                }""")

call(
    f"""aaaaaaaaaaaaaaaa
     bbbbbbbbbb {testeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee  # comment
                }"""
)

call(f"{
    aaaaaa
    + '''test
    more'''
}")

# Indentation

# What should be the indentation?
# https://github.com/astral-sh/ruff/discussions/9785#discussioncomment-8470590
if indent0:
    if indent1:
        if indent2:
            foo = f"""hello world
hello {
          f"aaaaaaa {
              [
                  'aaaaaaaaaaaaaaaaaaaaa',
                  'bbbbbbbbbbbbbbbbbbbbb',
                  'ccccccccccccccccccccc',
                  'ddddddddddddddddddddd'
              ]
          } bbbbbbbb" +
          [
              'aaaaaaaaaaaaaaaaaaaaa',
              'bbbbbbbbbbbbbbbbbbbbb',
              'ccccccccccccccccccccc',
              'ddddddddddddddddddddd'
          ]
      } --------
"""


# Implicit concatenated f-string containing quotes
_ = (
    'This string should change its quotes to double quotes'
    f'This string uses double quotes in an expression {"it's a quote"}'
    f'This f-string does not use any quotes.'
)

# Regression test for https://github.com/astral-sh/ruff/issues/14487
f"aaaaaaaaaaaaaaaaaaaaaaaaaa {10**27} bbbbbbbbbbbbbbbbbbbbbbbbbb ccccccccccccccccccccccccc"

# Regression test for https://github.com/astral-sh/ruff/issues/14778
f"{'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa' 'a' if True else ""}"
f"{'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa' 'a' if True else ""}"

# Quotes reuse
f"{'a'}"

# 312+, it's okay to change the outer quotes even when there's a debug expression using the same quotes
f'foo {10 + len("bar")=}'
f'''foo {10 + len("""bar""")=}'''

# 312+, it's okay to change the quotes here without creating an invalid f-string
f'{"""other " """}'
f'{"""other " """ + "more"}'
f'{b"""other " """}'
f'{f"""other " """}'


# Regression tests for https://github.com/astral-sh/ruff/issues/13935
f'{1: hy "user"}'
f'{1:hy "user"}'
f'{1: abcd "{1}" }'
f'{1: abcd "{'aa'}" }'
f'{1=: "abcd {'aa'}}'
f'{x:a{z:hy "user"}} \'\'\''

# Changing the outer quotes is fine because the format-spec is in a nested expression.
f'{f'{z=:hy "user"}'} \'\'\''


#  We have to be careful about changing the quotes if the f-string has a debug expression because it is inserted verbatim.
f'{1=: "abcd \'\'}'  # Don't change the outer quotes, or it results in a syntax error
f'{1=: abcd \'\'}'  # Changing the quotes here is fine because the inner quotes aren't the opposite quotes
f'{1=: abcd \"\"}'  # Changing the quotes here is fine because the inner quotes are escaped
# Don't change the quotes in the following cases:
f'{x=:hy "user"} \'\'\''
f'{x=:a{y:hy "user"}} \'\'\''
f'{x=:a{y:{z:hy "user"}}} \'\'\''
f'{x:a{y=:{z:hy "user"}}} \'\'\''

# This is fine because the debug expression and format spec are in a nested expression

f"""{1=: "this" is fine}"""
f'''{1=: "this" is fine}'''  # Change quotes to double quotes because they're preferred
f'{1=: {'ab"cd"'}}'  # It's okay if the quotes are in an expression part.


# Regression tests for https://github.com/astral-sh/ruff/issues/15459
print(f"{ {1, 2, 3} - {2} }")
print(f"{ {1: 2}.keys() }")
print(f"{({1, 2, 3}) - ({2})}")
print(f"{1, 2, {3} }")
print(f"{(1, 2, {3})}")


# Regression tests for https://github.com/astral-sh/ruff/issues/15535
print(f"{ {}, }")  # A single item tuple gets parenthesized
print(f"{ {}.values(), }")
print(f"{ {}, 1 }")  # A tuple with multiple elements doesn't get parenthesized
print(f"{  # Tuple with multiple elements that doesn't fit on a single line gets parenthesized
    {}, 1,
}")


# Regression tests for https://github.com/astral-sh/ruff/issues/15536
print(f"{ {}, 1, }")
