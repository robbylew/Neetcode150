# https://leetcode.com/problems/largest-rectangle-in-histogram/description/

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Initialize maxArea to keep track of the largest rectangle found.
        maxArea = 0
        # Initialize a stack to keep pairs of (index, height).
        stack = []

        # Iterate over each bar in the histogram.
        for i, h in enumerate(heights):
            start = i  # Initialize start as the current index.
            # While stack is not empty and the current height is less than the height of the top element of the stack.
            while stack and stack[-1][1] > h:
                # Pop the top element from the stack. This element represents the height and its first occurrence in the histogram.
                index, height = stack.pop()
                # Calculate the area with the popped height as the smallest height and update maxArea if it's larger.
                maxArea = max(maxArea, height * (i - index))
                # Update the start to the index of the popped element.
                start = index
            # Push the current start and height onto the stack.
            stack.append((start, h))

        # After processing all heights, calculate the area for the remaining elements in the stack.
        for i, h in stack:
            # The area is calculated using the height and the difference between the total length of the histogram and the index.
            maxArea = max(maxArea, h * (len(heights) - i))

        # Return the largest area found.
        return maxArea
