"""Reverses an integer value."""
# METHODS #######################################################################
def reverse(x):
    """
    :type num: int
    :rtype: int
    if >= 0: Just read it backwards using the third slice arg.
    if <= 0: Append -, take everything after 0, read backwards.
    """
    # Signed vs. Unsigned, Removes trailing 0's w/ cast.
    if x >= 0:
        result = int(str(x)[::-1])
    else:
        result = int('-' + str(x)[:0:-1])

    # Check validity.
    if abs(result) > 0x7FFFFFFF: # Hex 2147483647, -2147483648
        return 0

    return result

# MAIN #########################################################################

TEST_1 = 1534236469
TEST_2 = -1534236469
TEST_3 = 24380
TEST_4 = -62302349

print(reverse(TEST_1))
print(reverse(TEST_2))
print(reverse(TEST_3))
print(reverse(TEST_4))
