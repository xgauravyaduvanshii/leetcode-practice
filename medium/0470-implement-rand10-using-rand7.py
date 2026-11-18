# LeetCode 470. Implement Rand10() Using Rand7() — Medium
# https://leetcode.com/problems/implement-rand10-using-rand7/
# Submission 2198816459 — Accepted, Python3
#
# My thinking: two rand7 calls make 49 equally
# likely outcomes. I keep the first 40 and map them
# evenly onto 1 to 10, and throw away the other
# nine — that keeps every result equally likely.

class Solution:
    def rand10(self):
        while True:
            value = (rand7() - 1) * 7 + rand7()
            if value <= 40:
                return value % 10 + 1
