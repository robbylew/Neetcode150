# https://leetcode.com/problems/top-k-frequent-elements/description/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}  # Dictionary to count the frequency of each number in 'nums'
        freq = [[] for i in range(len(nums) + 1)]  # List of lists, where index represents frequency, to store numbers

        for n in nums:  # Count the frequency of each number in 'nums'
            count[n] = 1 + count.get(n, 0)  # Increment the count of the number 'n'
        for n, c in count.items():  # Iterate over the count dictionary
            freq[c].append(n)  # Append the number 'n' to its corresponding frequency index in 'freq'

        res = []  # List to store the top 'k' frequent numbers
        for i in range(len(freq) - 1, 0, -1):  # Iterate over 'freq' in reverse order (from highest frequency to lowest)
            for n in freq[i]:  # Iterate over numbers at the current frequency 'i'
                res.append(n)  # Add the number to the result list
                if len(res) == k:  # If 'k' numbers are added to the result, return the result
                    return res
