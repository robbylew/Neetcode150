# https://leetcode.com/problems/valid-parentheses/description/

class Solution:
    def isValid(self, s: str) -> bool:
        # This dictionary maps each closing bracket to its corresponding opening bracket.
        closeDict = {")" : "(", "}" : "{", "]": "["}

        # The stack is used to keep track of the opening brackets.
        stack = []

        # Iterating through each character in the string.
        for c in s:
            # If the character is not a closing bracket, it's an opening bracket.
            # So, we add it to the stack.
            if c not in closeDict:
                stack.append(c)
                continue
            
            # If the stack is empty (no opening bracket to match) or
            # the top element of the stack is not the matching opening bracket,
            # then the string is not valid.
            if not stack or stack[-1] != closeDict[c]:
                return False
            
            # If we find a matching pair of brackets, we remove the opening bracket
            # from the stack.
            stack.pop()

        # After processing all characters, if the stack is empty, all brackets were matched
        # and the string is valid. Otherwise, it's not.
        return not stack
