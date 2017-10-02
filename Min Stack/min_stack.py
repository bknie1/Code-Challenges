"""A simple Min Stack implementation."""
# pylint: disable=C0103
class MinStack(object):
    """
    A simple Min Stack implementation:
    push(item)
    pop()
    top()
    getMin()
    """
    def __init__(self):
        """
        Initializes the stack and maintains a length value for navigation.
        """
        self.stack = []
        self.length = len(self.stack)
        self.current_min = 0
################################################################################

    def push(self, item):
        """
        Pushes an arg value on to the stack.
        :type x: int
        :rtype: void
        """
        print("Pushing", item)

        current_min = self.getMin()     # Is the new item a min value?
        if current_min is None or item < current_min:
            self.current_min = item

        self.stack.append((item))       # Add to stack regardless.
        self.length = len(self.stack)   # Update length using new data.
################################################################################

    def pop(self):
        """
        Pops the top value off the stack (no args -> default -> top item).
        :rtype: void
        """
        popped = self.stack[-1]
        print("Popping", popped)
        self.stack.pop()                        # Defaults to last item.

        try:
            if self.current_min is popped:
                self.current_min = min(self.stack)
                print("New Min:", self.current_min)
        except:
            self.current_min = None

        self.length = len(self.stack)           # Update length using new data.
################################################################################

    def top(self):
        """
        Returns the top value of our stack.
        :rtype: int
        """
        if self.length == 0:
            return None

        print("Top Value:", self.stack[-1])
        return self.stack[-1]
################################################################################

    def getMin(self):
        """
        Returns the smallest value in the stack.
        :rtype: int
        """
        if self.length == 0:
            return None

        print("Min Value:", self.current_min)
        return self.current_min
# MAIN #########################################################################

# Your MinStack object will be instantiated and called as such:

OBJ = MinStack()

OBJ.push(-2)
OBJ.push(0)
OBJ.push(-3)
OBJ.pop()

PARAM_3 = OBJ.top()
PARAM_4 = OBJ.getMin()
