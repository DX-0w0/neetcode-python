'''
Max Consecutive Ones
Solved
Easy Company Tags

You are given a binary array nums, return the maximum number of consecutive 1's in the array.

Example 1:

Input: nums = [1,1,0,1,1,1]

Output: 3


Example 2:

Input: nums = [1,0,1,1,0,1]

Output: 2
'''

from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxValue=0
        count=0

        for ind, num in enumerate(nums):
            if num == 1: 
                count += 1
                maxValue = max(count, maxValue)
            else:
                count = 0
        
        
        return maxValue
    
class Solution2:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = cnt = 0
        for num in nums:
            cnt += 1 if num else -cnt
            res = max(res, cnt)
        return res    
    
# Create an instance of the class
solution = Solution()

# Call the method
result = solution.findMaxConsecutiveOnes([1,1,0,1,1,1])
print(result)
