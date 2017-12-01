"""A simple quicksort implementation."""

# METHODS ######################################################################

def quicksort(values, start, end):
    """
    Choose a pivot value: Middle in each partition.
    Sort Parts: Apply quicksort algorithm recursively to the left/right parts.
    """
    print("Values:", values)
    print("Start:", values[start])
    print("End:", values[end])
    if start < end:                             # 2+ elements?
        split = partition(values, start, end)   # Partition
        quicksort(values, start, split - 1)     # And sort (left).
        quicksort(values, split, end)           # And sort (right).

################################################################################
def partition(values, start, end):
    """
    Partition:
        Rearrange elements in such a way, that all elements which are
        lesser than the pivot go to the left part of the array and all elements
        greater than the pivot, go to the right part of the array. Values equal
        to the pivot can stay in any part of the array.
    """
    pivot = values[end] # Our comparison value.
    print("Pivot", pivot)
    i, j = start, end # i, j will walk towards each other.

    while i < j: # Until we cross paths...
        while i < j: # Walk i towards j. Look for swap opportunities.
            if values[i] > pivot:
                values[i], values[j] = values[j], values[i]
                break
            i += 1

        while j > i:
            if values[j] < pivot: # Walk j towards i. Look for swap opportunities.
                values[j], values[i] = values[i], values[j]
                break
            j -= 1

    values[j] = pivot # Place pivot in final position; where i, j collide.
    return j          # This is where we need to split our list of values!
# MAIN #########################################################################

VALUES = [5, 3, 6, 7, 10, 13, 17, 2, 9]

START = 0
END = len(VALUES) - 1
quicksort(VALUES, START, END)
