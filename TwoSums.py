"""Given a target value and list of integers,
find the indices of two values who's sum reaches a given target."""

# f(x)

def two_sum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    result_dict = {}
    for i in range(len(nums)): # C0200
        aim = target - nums[i]
        if aim in result_dict:
            return result_dict[aim], i
        else:
            if not nums[i] in result_dict:
                result_dict[nums[i]] = i
# MAIN

NUMS1 = [3, 2, 4]
TARGET1 = 6

NUMS2 = [-1, -2, -3, -4, -5]
TARGET2 = -8

print(two_sum(NUMS1, TARGET1))
print(two_sum(NUMS2, TARGET2))
