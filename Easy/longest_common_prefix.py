"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
"""

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest_string = min(strs)

        for i, char in enumerate(shortest_string):
            for other_string in strs:
                if other_string[i] != char:
                    return shortest_string[:i]

        return shortest_string
