# https://leetcode.com/problems/encode-and-decode-strings/description/

class Solution:
    def encode(self, strs):
        res = ""  # Initialize an empty string to store the encoded result
        for s in strs:  # Loop through each string in the list
            res += str(len(s)) + "#" + s  # Add the length of the string, followed by '#' and the string itself

        return res  # Return the encoded string

    def decode(self, s):
        res = []  # Initialize an empty list to store the decoded strings
        i = 0  # Start index for parsing the encoded string

        while i < len(s):  # Continue until the end of the encoded string is reached
            j = i
            while s[j] != '#':  # Find the position of '#' to separate length from the string
                j += 1
            length = int(s[i:j])  # Extract the length of the next string
            i = j + 1  # Move past '#' to the start of the actual string
            j = i + length  # Calculate the end position of the string
            res.append(s[i:j])  # Extract and append the string to the result list
            i = j  # Update the start index for the next string
            
        return res  # Return the list of decoded strings
