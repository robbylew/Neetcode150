# https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Initialize a result list with the same length as 'temperatures', filled with 0s.
        # Each element in 'res' will eventually hold the number of days until a warmer temperature.
        res = [0] * len(temperatures)

        # Initialize an empty stack. This stack will store pairs (temperature, index).
        stack = []

        # Iterate over the list 'temperatures' with both index and value.
        for i, t in enumerate(temperatures):
            # While stack is not empty and the current temperature 't' is greater than
            # the temperature at the top of the stack (i.e., the last recorded temperature
            # which hasn't found a warmer day yet):
            while stack and t > stack[-1][0]:
                # Pop the top element from stack. It contains the temperature and index
                # of a day for which we've now found a warmer day.
                stackT, stackInd = stack.pop()

                # Calculate the number of days until a warmer temperature and update the
                # corresponding index in the 'res' list.
                res[stackInd] = i - stackInd

            # Push the current temperature and its index onto the stack.
            # This is for tracking the next day that will have a higher temperature than this one.
            stack.append((t, i))

        # Return the populated 'res' list, which now contains the number of days until
        # a warmer temperature for each day in the input list.
        return res
