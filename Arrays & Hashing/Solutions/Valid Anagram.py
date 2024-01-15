# https://leetcode.com/problems/valid-anagram/description/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # First, check if the lengths of the two strings are equal. 
        # If they are not, they cannot be anagrams, so return False.
        if len(s) != len(t):
            return False

        # Initialize two dictionaries to count the occurrences of each character in both strings.
        countS, countT = {}, {}

        # Iterate over the length of the string (both strings have the same length).
        for i in range(len(s)):
            # For each character in string s, add to its count in countS.
            # The get method is used to handle characters that haven't been seen yet.
            countS[s[i]] = 1 + countS.get(s[i], 0)

            # Similarly, for each character in string t, add to its count in countT.
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        # After counting characters in both strings, 
        # check if the two dictionaries are identical.
        # If they are, s and t are anagrams of each other.
        return countS == countT

