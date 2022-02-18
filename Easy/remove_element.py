"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
The relative order of the elements may be changed.
"""

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums != 0:
            nums.remove(val)

        counter = len(nums)

        return counter
