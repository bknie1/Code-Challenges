"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    if head.next is None:
        return False # There is no LL.
    else:
         # Starting nodes.
        slower = head.next
        faster = head.next.next
        # Detect End
        while(slower != None or faster != None):
            
            # Cycle detected?
            if slower is faster:
                return True
            
            # Otherwise, Proceed
            slower = tortoise(slower) # Next
            faster = hare(faster) # Next * 2
            
        return False # We reached the end with no cycle.
    # pass
    
def tortoise(node):
    # Moves slower: One at a time.
    return node.next

def hare(node):
    # Jumps ahead so, if there's a cycle, we'll loop back faster.
    return node.next.next 