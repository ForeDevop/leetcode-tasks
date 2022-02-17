"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, value in enumerate(nums):
            remaining = target - nums[i]

            if remaining in seen:
                return [seen[remaining], i]

            seen[value] = i
