'''
Score of a String
Solved

You are given a string s. The score of a string is defined as the sum of the absolute difference between the ASCII values of adjacent characters.

Return the score of s.

Example 1:

Input: s = "code"

Output: 24

Explanation: The ASCII values of the characters in the given string are: 'c' = 99, 'o' = 111, 'd' = 100, and 'e' = 101. The score of s will be: |111 - 99| + |100 - 111| + |101 - 100|.

Example 2:

Input: s = "neetcode"

Output: 65
'''


class Solution:
    def scoreOfString(self, s: str) -> int:
        sum=0
        for i in range(len(s)-1):
            cur=ord(s[i])
            next=ord(s[i+1])
            aSum = abs(cur-next)
            sum+=aSum
            
        return sum
            
# Create an instance of the class
solution = Solution()

# Call the method   
result = solution.scoreOfString("code")
print(result)