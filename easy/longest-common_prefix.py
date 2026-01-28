'''
Longest Common Prefix
Solved
Easy Company Tags

You are given an array of strings strs. Return the longest common prefix of all the strings.

If there is no longest common prefix, return an empty string "".

Example 1:

Input: strs = ["bat","bag","bank","band"]

Output: "ba"

Example 2:

Input: strs = ["dance","dag","danger","damage"]

Output: "da"

Example 3:

Input: strs = ["neet","feet"]

Output: ""

Constraints:

    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] is made up of lowercase English letters if it is non-empty.


'''

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ''
        shortest_word = min(strs, key=len, default="")
        
        for i in range(len(shortest_word)):
            letter = shortest_word[i]

            status = all(word[i] == letter for word in strs)
            if not status: 
                return result
            result += letter

        return result        
    
# Create an instance of the class
solution = Solution()   

# Call the method
result = solution.longestCommonPrefix(["flower","flow","flight"])
print(result)