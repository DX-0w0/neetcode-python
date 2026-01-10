'''
Valid Word Square
Solved

Given an array of strings words, return true if it forms a valid word square.

A sequence of strings forms a valid word square if the kth row and column read the same string, where 0 <= k < max(numRows, numColumns).

Example 1:

Input: words = ["abcd",
                "bnrt",
                "crmy",
                "dtye"]

Output: true

Explanation:
The 1st row and 1st column both read "abcd".
The 2nd row and 2nd column both read "bnrt".
The 3rd row and 3rd column both read "crmy".
The 4th row and 4th column both read "dtye".
Therefore, it is a valid word square.

Example 2:

Input: words = ["abcd",
                "bnrt",
                "crm",
                "dt"]

Output: true
'''

class Solution:
    def validWordSquare(self, words: list[str]) -> bool:
        for i, word in enumerate(words):
            for j, char in enumerate(word):
                if j >= len(words) or i >= len(words[j]) or char != words[j][i]:
                    return False
        return True
    
# Create an instance of the class
solution = Solution()   

# Call the method   
result = solution.validWordSquare(["abcd", "bnrt", "crmy", "dtye"])
print(result)