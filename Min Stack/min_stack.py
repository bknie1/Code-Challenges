"""A simple Min Stack implementation."""
class MinStack(object):
    """
    A simple Min Stack implementation:
    push(item)
    pop()
    top()
    get_min()
    """
    def __init__(self):
        """
        Initializes the stack and maintains a length value for navigation.
        """
        self.stack = []
################################################################################

    def push(self, item):
        """
        Pushes an arg value on to the stack.
        :type item: int
        :rtype: void
        """
        print("Pushing", item)
        current_min = self.get_min()
        if current_min is None or item < current_min:
            current_min = item
        self.stack.append(item)
################################################################################

    def pop(self):
        """
        Pops the top value off the stack (default, no args).
        :rtype: void
        """
        print("Popping", self.stack[-1])
        self.stack.pop() # Defaults to last item.
################################################################################

    def top(self):
        """
        Returns the top value of our stack.
        :rtype: int
        """
        length = len(self.stack)
        if length == 0:
            return None

        print("Top Value:", self.stack[-1])
        return self.stack[-1]
################################################################################

    def get_min(self):
        """
        Returns the smallest value in the stack.
        :rtype: int
        """
        length = len(self.stack)
        if length == 0:
            return None

        print("Min Value:", min(self.stack))
        return min(self.stack)
# MAIN #########################################################################

# Your MinStack object will be instantiated and called as such:

OBJ = MinStack()

OBJ.push(-2)
OBJ.push(0)
OBJ.push(-3)
OBJ.pop()

PARAM_3 = OBJ.top()
PARAM_4 = OBJ.get_min()
