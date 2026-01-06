"""
Contains Duplicate
Solved

Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true


Example 2:

Input: nums = [1, 2, 3, 4]

Output: false
"""


from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for x in nums:
            if x in seen: return True
            seen.add(x)
        return False
                
class Solution2:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
    

# Create an instance of the class
solution = Solution()   

# Call the method
result = solution.hasDuplicate([1,2,3,4,5,1])
print(result)