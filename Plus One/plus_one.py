"""Given a non-negative list representing an integer, add 1 to that integer."""
# METHODS #######################################################################
def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    Use the value indices to determine and multiply by place value.
    1. Increment the least significant digit.
    2. Reverse the order of the digits list for place value compatability.
    3. Walk backwards and create a new output sum by multiplying digits by place.
    4. Divide the return output into a single digit list.
    """
    output = 0
    digits[len(digits) - 1] += 1
    digits = digits[::-1]
    for i in range(len(digits) - 1, -1, -1):
        output += digits[i] * pow(10, i)
    return list(map(int, str(output)))

################################################################################

# MAIN #########################################################################

TEST_1 = [0]
TEST_2 = [3, 0, 0, 0]
TEST_3 = [9]
TEST_4 = [9, 9, 9]

print("1:", plusOne(TEST_1))
print("2:", plusOne(TEST_2))
print("3:", plusOne(TEST_3))
print("4:", plusOne(TEST_4))
