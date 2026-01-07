'''
Length Of Last Word
Solved

You are given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

Note: A substring is a contiguous non-empty sequence of characters within a string.

Example 1:

Input: s = "Hello World"

Output: 5

Explanation: The last word is "World" with length 5.

Example 2:

Input: s = "   fly me   to   the moon  "

Output: 4

Explanation: The last word is "moon" with length 4.
'''

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        last = words.pop()
        return len(last)
    

# Create an instance of the class
solution = Solution()

# Call the method
result = solution.lengthOfLastWord("Hello World")
print(result)
