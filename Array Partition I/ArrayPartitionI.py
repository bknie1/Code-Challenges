# The goal is to get the largest possible sum of MIN of the pair.
# So for the example [1, 2, 3, 4],
# the best pairs are (1, 2) and (3, 4).
# min(1, 2) + min(3, 4) = 1 + 3 = 4

def arrayPairSum(nums):
    """
    :type nums: List[int]
    :rtype: int

    # This takes the whole string ([::])
    # And it takes every other character (2)
    """
    # Sorts the string.
    # Slices off every other value using the stride slice arg.
    # This emulates what would have been our min pairing.
    # The left value is always less than the right.
    # So we grab the first element from the first two would be pairs.
    nums = sorted(nums)
    nums = nums[::2]
    min_sum = sum(nums)
    return min_sum

# MAIN

TEST_1 = [1, 4, 3, 2]   # O: 4 = 1 + 3
TEST_2 = [10, 8, 6, 15] # O: 16 = 10 + 6
TEST_3 = [1, 2, 3, 2]      # O: 1 + 3 = 4

# print(arrayPairSum(TEST_1))
# print(arrayPairSum(TEST_2))
print(arrayPairSum(TEST_3))
