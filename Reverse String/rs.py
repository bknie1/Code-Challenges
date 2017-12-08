"""Simple, Pythonic reverse string."""
def reverse_string(text):
    """
    :type s: str
    :rtype: str
        """
    return text[::-1]
    """
    result = ""
    for i in text:
        result = i + result

    return result
    """

reverse_string("hello")
