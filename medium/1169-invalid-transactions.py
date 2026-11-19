# LeetCode 1169. Invalid Transactions — Medium
# https://leetcode.com/problems/invalid-transactions/
# Submission 2199008903 — Accepted, Python3
#
# My thinking: a transaction is invalid when its
# amount is over a thousand, or when the same
# person spent in another city within an hour
# of it. I check every transaction against all
# the others.

from typing import List


class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        parsed = []
        for t in transactions:
            name, time, amount, city = t.split(",")
            parsed.append((name, int(time), int(amount), city))
        invalid = []
        for i, (name, time, amount, city) in enumerate(parsed):
            if amount > 1000:
                invalid.append(transactions[i])
                continue
            for j, (other_name, other_time, _, other_city) in enumerate(parsed):
                if i != j and other_name == name and other_city != city and abs(other_time - time) <= 60:
                    invalid.append(transactions[i])
                    break
        return invalid
