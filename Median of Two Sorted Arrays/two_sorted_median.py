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
    Cut each array into two halves and use max/min to find the median.
"""
# METHODS ######################################################################

def find_median_of_sorted(nums_1, nums_2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """

    return walk_lists()
################################################################################
def walk_lists():
    """
    Walk the two lists recursively to find the median.
    """
    # Break out condition.

    # Walk condition.

    return # median
# MAIN #########################################################################

NUMS_1 = [1, 3]
NUMS_2 = [2]
NUMS_3 = [1, 2]
NUMS_4 = [3, 4]
NUMS_5 = [1, 2, 4, 7, 9]
NUMS_6 = [3, 5, 6, 8]

print(find_median_of_sorted(NUMS_2, NUMS_3))
