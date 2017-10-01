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
"""

# pylint: disable=C0103, R0913

# METHODS ######################################################################

def find_median_of_sorted(nums_1, nums_2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float

    Find the kth element in two sorted arrays of differing length where k is
    our median index/indices.

    1. Find the total length of our would be array.
    2. Get median index of each.
        - We know k will be the middle value of an odd number of elements.
            - median index = n // 2
        - K will be the middle two values of an even number of elements.
            - greater middle = n // 2
            - lesser middle = n // 2 - 1
            - median = (g + l) / 2
    """
    total_len = len(nums_1 + nums_2)
    print("Total Length:", total_len)
     # Odd, so we only need the mid index.
    if total_len % 2 == 1:
        print("Odd list k.")
        median = find_k(nums_1, nums_2, total_len // 2)
    # Even, so we need to pass in both the lesser and greater mid indices.
    else:
        print("Even list k.")
        median = (find_k(nums_1, nums_2, total_len // 2) +
                  find_k(nums_1, nums_2, total_len // 2 - 1) / 2)
    return median
################################################################################
def find_k(a, b, k):
    """
    We can use the calculated indices to find the median values.
    Narrow down the median's location (k) by using the calculated median of each
    list by splitting each list into two parts and only continuing with the
    parts we know contain the potential median for both:
    A1 --> [A0 ... A(n//2)]  [A (n/2 + 1) ... A n-1] <-- A2
    B1 --> [B0 ... B(m//2)]  [B (m/2 + 1) ... B m-1] <-- B2

    Example:
        1.) How did we calculate our k?
            [1, 2, 3, 4, 5] [3, 4, 5, 6] = [1, 2, 3, 4, 5, 3, 4, 5, 6]
                                                        ^ 4th element is mid.

        2.) Where might k be located in our sorted arrays?

            Is (a_len / 2 + b_len / 2) < k?
                - Keep A2, B2: It's in the right part of our lists.
                - Toss A1, B1: It's not in the left part of our lists.
            Else, (a_len / 2 + b_len / 2) > k?
                - Keep A1, B1: It's in the left part of our lists.
                - Toss A2, B2: It's not in the right part of our lists.

            k = 4, the median index of our hypothetical combined list.
            a_len = 5
            b_len = 4

            2.5 + 2 = 4.5
                (5 / 2) = 2.5
                (4 / 2) = 2

            [1, 2, 3, 4, 5, 3, 4, 5, 6]
                         ^
            We know our actual k must be to the left because k >= mid sum.

            4 is >= than our k; 4.
                - Our k must be in the left part of our lists.
                - [1, 2, 3, 4, 5] [3, 4, 5, 6]

        3.) Slice and return, try again until we eliminate a list.
    """
    # If we're missing a list we can assume k of the opposite is our median.
    print("\n")
    if not a:
        print("Only b remains.")
        return b[k]
    if not b:
        print("Only a remains.")
        return a[k]

    a_mid, b_mid = len(a) // 2, len(b) // 2 # Find mid of each list.
    mid_sum = a_mid + b_mid

    print("k:\t\t", k)
    print("A mid index:\t", a_mid, "\nB mid index:\t", b_mid)
    print("Mid index sum:\t", mid_sum)

    print("\nCOMPARING K TO SUM OF MID INDICES.\t",
          k, "vs.", mid_sum)

    if mid_sum < k:
        print("LARGER K\n")
        # A should always be the larger list, B smaller. Slice and call.
        print("COMPARING MID INDICES",
              "\t\t\t", a[a_mid], "vs.", b[b_mid])
        if a[a_mid] > b[b_mid]:
            print("LARGER A: KEEP B RIGHT")
            return find_k(a, b[b_mid + 1:], k - b_mid - 1)
        # else: a[a_mid] <= b[b_mid]
        print("LARGER/EQUAL B: KEEP A RIGHT")
        return find_k(a[a_mid + 1:], b, k - a_mid - 1)
    else: # mid_sum >= k
        print("SMALLER/EQUAL K\n")
        # A should always be the larger list, B smaller. Slice and call.
        print("COMPARING MID VALUES",
              "\t\t\tA mid value:", a[a_mid], "vs.", "B mid value:", b[b_mid])
        if a[a_mid] > b[b_mid]:
            print("LARGER A: KEEP A LEFT")
            return find_k(a[:a_mid], b, k)
        # else: a[a_mid] <= b[b_mid]
        print("LARGER/EQUAL B: KEEP B LEFT")
        return find_k(a, b[:b_mid], k)
# MAIN #########################################################################
# Odd example of initial k's.
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
#  0  1  2  3 [4] 5  6  7  8

# Even example of initial k's.
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#  0  1  2  3 [4  5] 6  7  8  9

NUMS_1 = [1, 3]
NUMS_2 = [2]
NUMS_3 = [1, 2]
NUMS_4 = [3, 4]
NUMS_5 = [1, 2, 3, 4, 5]
NUMS_6 = [3, 4, 5, 6]

print(find_median_of_sorted(NUMS_5, NUMS_6))
