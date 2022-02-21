"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Given a roman numeral, convert it to an integer.
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        dig = 0
        for i in range(len(s) - 1):
            if roman_to_int[s[i]] >= roman_to_int[s[i + 1]]:
                dig += roman_to_int[s[i]]
            else:
                dig -= roman_to_int[s[i]]

        dig += roman_to_int[s[len(s) - 1]]

        return dig
