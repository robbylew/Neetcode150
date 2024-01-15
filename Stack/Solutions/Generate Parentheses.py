# https://leetcode.com/problems/generate-parentheses/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Initialize a list `stack` to keep track of the current sequence of parentheses,
        # and a list `res` to store the final results (valid combinations).
        stack = []
        res = [] 

        def Backtrack(openN, closedN):
            # Base case: If the number of open and closed parentheses are both equal to `n`,
            # it means a valid combination is formed. Join the stack into a string and add to results.
            if openN == closedN == n:
                res.append("".join(stack))
                return

            # If the number of open parentheses is less than `n`, we can add an open parenthesis.
            # After adding, we recursively call the function to continue building the sequence.
            # After the recursive call returns, we pop the last element to backtrack.
            if openN < n:
                stack.append("(")
                Backtrack(openN + 1, closedN)
                stack.pop()

            # If the number of closed parentheses is less than the number of open parentheses,
            # we can add a closed parenthesis. This ensures we never have more closed than open
            # parentheses at any point, keeping the sequence valid.
            # Similar to the open parenthesis, we backtrack after the recursive call.
            if closedN < openN:
                stack.append(")")
                Backtrack(openN, closedN + 1)
                stack.pop()

        # Start the backtracking process with 0 open and 0 closed parentheses.
        Backtrack(0, 0)

        # Return the list of valid combinations.
        return res
