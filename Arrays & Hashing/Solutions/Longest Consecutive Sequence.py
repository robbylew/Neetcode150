# https://leetcode.com/problems/longest-consecutive-sequence/description/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)  # Convert the list of numbers into a set for O(1) lookups
        longest = 0  # Initialize the longest sequence length to 0

        for n in numSet:  # Iterate through each number in the set
            if (n - 1) not in numSet:  # Check if the previous number (n - 1) is not in the set. If it's not, 'n' is a potential start of a new sequence
                length = 1  # Initialize the current sequence length to 1
                while (length + n) in numSet:  # Continue checking the presence of consecutive numbers in the set
                    length += 1  # Increment the length for each consecutive number found
                longest = max(length, longest)  # Update the longest sequence length if the current sequence is longer

        return longest  # Return the length of the longest consecutive sequence
