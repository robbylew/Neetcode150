# https://leetcode.com/problems/min-stack/

class MinStack:

    def __init__(self):
        # Two stacks are used: one for storing all the values ('stack')
        # and the other for keeping track of the minimum value at each state ('minStack').
        self.minStack = []
        self.stack = []
        
    def push(self, val: int) -> None:
        # When a new value is pushed, it's added to the 'stack'.
        self.stack.append(val)
        # The new value is compared with the current minimum (top of 'minStack').
        # If 'minStack' is empty or the new value is smaller, 'val' becomes the new minimum.
        # Otherwise, the current minimum is appended to 'minStack' again.
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)
        
    def pop(self) -> None:
        # When popping, remove the top element from both 'stack' and 'minStack'.
        # This ensures that the current minimum is discarded if it was the top element.
        self.stack.pop()
        self.minStack.pop()
        
    def top(self) -> int:
        # Returns the top element of 'stack' without removing it.
        # This is the last added element.
        return self.stack[-1]
        
    def getMin(self) -> int:
        # Returns the current minimum value, which is the top of 'minStack'.
        # Since 'minStack' is updated with each push operation, this is always the current minimum.
        return self.minStack[-1]
