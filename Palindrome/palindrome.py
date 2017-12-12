"""Palindrome Detector"""

def is_palindrome(num):
    """
    Breaks if values don't match.
    """
    num = str(num)
    start = 0
    end = len(num) - 1

    while start < end:
        print(num[start], num[end])
        if num[start] != num[end]:
            return False
        start += 1
        end -= 1

    return True

# MAIN

print(is_palindrome(354453))
print(is_palindrome(74547))
print(is_palindrome(74565547))
print(is_palindrome(2147483647))
print(is_palindrome(-2147447412))
