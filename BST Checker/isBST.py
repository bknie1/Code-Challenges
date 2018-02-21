""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""
INT_MIN = -4294967296
INT_MAX = 4294967296

def checkBST(root):
    return isBST(root, INT_MIN, INT_MAX)

def isBST(n, min, max):
    # Does this node actually exist or are we done?
    if n is None:
        return True

    # It exists, so compare it to the previous node's data. Does it fail the BST test?
    # print("Min: " + str(min) + "\nMax: " + str(max))
    if n.data < min or n.data > max:
        return False

    # No? Let's move on to processing the children.
    # AND the result so we can check for success/failure in either case.
    # e.g. we progress to 2 and 6 against our current 4. New max becomes 3, new min becomes 5.
    return isBST(n.left, min, n.data - 1) and isBST(n.right, n.data + 1, max)
