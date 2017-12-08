"""
Given an array of integers, every element appears twice except for one.
Find that single one.

Note:
Your algorithm should have a linear runtime complexity.
Could you implement it without using extra memory?
"""
def single_number(nums):
    """
    We try to pop existing values off of our hash table. Otherwise, we add it.
    Ultimately, if a duplicate exists in nums, it is also in the hash table, and
    that i we're dealing with doesn't get added anyway. Instead, we're left with
    a single value in our table; the single number in our problem.

    Technically, we could also use this to detect all single numbers, but we would
    probably want to return table[:n-1] or something.
    """
    table = {}
    for i in nums:
        try:
            table.pop(i)
        except:
            table[i] = 1
    return table.popitem()[0]

###############################################################################
TEST_1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 6, 6, 7, 7]
print(single_number(TEST_1))
