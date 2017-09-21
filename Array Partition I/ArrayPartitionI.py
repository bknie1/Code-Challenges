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
    # Sorts the string but only keeps every other value.
    # The last slice parameter is called a stride (2 here).
    # This emulates what would have been our min pairing.
    # The left value is always less than the right.
    # So we grab the first element from the first two would be pairs.
    nums = sorted(nums[::2])
    return sum(nums)

# MAIN

TEST_1 = [1, 4, 3, 2]   # O: 4 = 1 + 3
TEST_2 = [10, 8, 6, 15] # O: 16 = 10 + 6

print(arrayPairSum(TEST_1))
print(arrayPairSum(TEST_2))
