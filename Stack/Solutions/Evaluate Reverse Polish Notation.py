# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []  # Initiate stack to store the numbers.

        # Iterate through each token in the RPN expression.
        for c in tokens:
            # If the token is a '+', pop the top two elements from the stack,
            # add them, and push the result back onto the stack.
            if c == "+":
                stack.append(stack.pop() + stack.pop())

            # If the token is a '-', pop the top two elements (a, b),
            # subtract them as (b - a), and push the result back onto the stack.
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)

            # If the token is a '*', pop the top two elements from the stack,
            # multiply them, and push the result back onto the stack.
            elif c == "*":
                stack.append(stack.pop() * stack.pop())

            # If the token is a '/', pop the top two elements (a, b),
            # divide them as float and convert to int for floor division,
            # then push the result back onto the stack.
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))

            # If the token is a number, convert it to an integer and
            # push it onto the stack.
            else:
                stack.append(int(c))

        # After processing all tokens, the result is the only element in the stack.
        return stack[0]
