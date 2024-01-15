# https://leetcode.com/problems/product-of-array-except-self/description/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)  # Initialize the result list with 1s, as the base for multiplication

        prefix = 1  # Initialize a prefix product variable
        for i in range(len(nums)):  # Iterate over the list
            res[i] *= prefix  # Multiply the current prefix product to the result list
            prefix *= nums[i]  # Update the prefix product by multiplying it with the current number

        postfix = 1  # Initialize a postfix product variable
        for i in range(len(nums) - 1, -1, -1):  # Iterate over the list in reverse
            res[i] *= postfix  # Multiply the current postfix product to the result list
            postfix *= nums[i]  # Update the postfix product by multiplying it with the current number

        return res  # Return the final result list
