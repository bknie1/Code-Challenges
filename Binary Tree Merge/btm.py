"""Binary Tree Merge"""

def mergeTrees(self, t1, t2):
    """
    :type t1: TreeNode
    :type t2: TreeNode
    :rtype: TreeNode
    """
    # If neither t1 nor t2 exist we don't have anything to merge.
    if not t1 and not t2:
        return None
    # Otherwise, we make a new tree node using the contents of t1, t2, if they exist.
    node = TreeNode((t1.val if t1 else 0) + (t2.val if t2 else 0))
    # We go ahead and merge the children to create our new left child.
    node.left = self.mergeTrees(t1 and t1.left, t2 and t2.left)
    # We do the same for the right child.
    node.right = self.mergeTrees(t1 and t1.right, t2 and t2.right)
    return node
