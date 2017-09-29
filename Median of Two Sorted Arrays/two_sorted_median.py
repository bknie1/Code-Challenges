"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should
be O(log (m+n)).

Example 1:
    nums1 = [1, 3]
    nums2 = [2]

    The median is 2.0

Example 2:
    nums1 = [1, 2]
    nums2 = [3, 4]

    The median is (2 + 3)/2 = 2.5

Ideas:
    Find the median of both. This is our range because the median will be
    somewhere between the two values. Recursively call and walk towards one
    another. Direction depends on which array has the greater value.
"""

# METHODS

def find_median_of_sorted(nums_1, nums_2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    mid_1 = len(nums_1) // 2
    mid_2 = len(nums_2) // 2

    print("List 1:", nums_1, "\t\tMid Index 1:", mid_1, "\t\tMid:", nums_1[mid_1])
    print("List 2:", nums_2, "\t\tMid Index 2:", mid_2, "\t\tMid:", nums_2[mid_2], "\n")

    median = (nums_1[mid_1] + nums_2[mid_2]) / 2
    print("Potential Median:", median)

    if mid_1 == 0 or mid_2 == 0:
        print("Median:", median)
        return median

    if nums_1[mid_1] < nums_2[mid_2]:
        print("mid 1 < mid 2")
        find_median_of_sorted(nums_1[mid_1:], nums_2[:mid_2])
    else:
        print("mid 1 > mid 2")
        find_median_of_sorted(nums_2[mid_2:], nums_1[mid_1:])

# MAIN

NUMS_1 = [1, 3]
NUMS_2 = [2]
NUMS_3 = [1, 2]
NUMS_4 = [3, 4]

print(find_median_of_sorted(NUMS_3, NUMS_4))
