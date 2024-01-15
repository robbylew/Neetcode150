# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # A dictionary to store numbers and their indices

        for i, n in enumerate(nums):  # Loop through the list, with 'i' as the index and 'n' as the number
            newTarget = target - n  # Calculate the complementary number needed to reach the target
            if newTarget in prevMap:  # Check if this complementary number exists in the map
                return [prevMap[newTarget], i]  # If it exists, return the indices of the two numbers
            prevMap[n] = i  # Store the current number and its index in the map

        # If no such pair is found, the function will end without a return statement
        # In the context of LeetCode, this is fine as the problem statement guarantees at least one solution



        