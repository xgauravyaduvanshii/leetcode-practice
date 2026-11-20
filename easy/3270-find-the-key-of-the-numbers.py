# 3270. Find the Key of the Numbers (Easy)
# https://leetcode.com/problems/find-the-key-of-the-numbers/
# Submission 2199991247 — Accepted, Python3
class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        # My thinking: write each number as four digits,
        # then for each place take the smallest of the
        # three digits. Those four smallest digits, in
        # order, make the key — leading zeroes drop off
        # when it becomes a number.
        key = ""
        for a, b, c in zip(f"{num1:04d}", f"{num2:04d}", f"{num3:04d}"):
            key += min(a, b, c)
        return int(key)
