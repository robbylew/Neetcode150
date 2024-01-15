# https://leetcode.com/problems/contains-duplicate/description/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Create a hashset where we store very integer in the nums list.
        hashset = set()

        # Iterate through every integer in the list nums.
        for n in nums:
            # If the number already exists in the hashset, then it has to be a duplicate so we return True.
            if n in hashset:
                return True
            # Otherwise we add the new integer to the hashset.
            hashset.add(n)
        # If no duplicates were found, then we return False.
        return False
        