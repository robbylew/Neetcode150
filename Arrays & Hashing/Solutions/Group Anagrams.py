# https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)  # Creates a default dictionary where each value is initialized as a list

        for s in strs:  # Iterate through each string in the list
            count = [0] * 26  # Initialize a list of 26 zeros, representing the count of each letter (assuming lowercase English letters)

            for c in s:  # Iterate through each character in the string
                count[ord(c) - ord("a")] += 1  # Increment the count of the letter in the count array

            ans[tuple(count)].append(s)  # Convert the count array to a tuple (as it's hashable) and use it as a key in the dictionary. Append the current string to the list of strings that have the same character count.

        return ans.values()  # Return the values of the dictionary, which are lists of grouped anagrams