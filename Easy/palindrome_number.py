"""
Given an integer x, return true if x is palindrome integer.
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        array_of_nums = [int(nums) for nums in str(x)]
        rev_array_of_nums = [int(nums) for nums in str(x)]
        rev_array_of_nums.reverse()

        if array_of_nums == rev_array_of_nums:
            return True

        return False
