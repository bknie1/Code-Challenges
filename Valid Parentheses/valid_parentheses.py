"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid
but "(]" and "([)]" are not.
"""
def is_valid(test):
    """
    :type s: str
    :rtype: bool
    Replaces all valid pairings with empty strings.
    If there's a remaining length it means there was an invalid pair.
    """
    test = test.replace("()", "")
    test = test.replace("[]", "")
    test = test.replace("{}", "")

    length = len(test)
    if length <= 0:
        return True # Everything (valid pairs) replaced, nothing left.
    return False # There's a remaining length. Not everything was replaced.

TEST_1 = "(){}[]{}()[]"
TEST_2 = "()[]{]}([})"

print(is_valid(TEST_1))
print(is_valid(TEST_2))
