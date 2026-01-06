"""
Replace Elements With Greatest Element On Right Side
Solved

You are given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.

Example 1:

Input: arr = [2,4,5,3,1,2]

Output: [5,5,3,2,2,-1]

Example 2:

Input: arr = [3,3]

Output: [3,-1]

Constraints:

    1 <= arr.length <= 10,000
    1 <= arr[i] <= 100,000
"""


class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        result = []
        for i in range(len(arr)):
            subarr = arr[i + 1 :]
            maxNum = max(subarr, default=-1)
            result.append(maxNum)

        return result


# Create an instance of the class
solution = Solution()

# Call the method
result = solution.replaceElements([2,4,5,3,1,2])
print(result)  
