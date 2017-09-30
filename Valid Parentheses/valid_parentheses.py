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
    True = remaining length, invalid.
    False = No remaining length, valid.
    """
    length = len(test)
    while length != 0 and length % 2 == 0:
        test = test.replace("()", "")
        test = test.replace("[]", "")
        test = test.replace("{}", "")

        if length > len(test): # Accounts for replaced values.
            length = len(test)
        else:               # If no change, then we're out of text.
            length = 0
    return not bool(len(test)) # Remaining length determines validity.

TEST_1 = "(){}[]{}()[]"
TEST_2 = "()[]{]}([})"
TEST_3 = "([])"
TEST_4 = "(("
TEST_5 = "["

print(is_valid(TEST_1))
print(is_valid(TEST_2))
print(is_valid(TEST_3))
print(is_valid(TEST_4))
print(is_valid(TEST_5))
