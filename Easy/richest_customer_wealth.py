"""
You are given an m x n integer grid accounts where accounts[i][j]
is the amount of money the i customer has in the j bank.
Return the wealth that the richest customer has.
"""

from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth_so_far = -1
        for account in accounts:
            cur_customer_weatlh = sum(account)
            max_wealth_so_far = max(max_wealth_so_far, cur_customer_weatlh)

        return max_wealth_so_far


class ShortSolution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(account) for account in accounts)
