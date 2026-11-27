# LeetCode 38. Count and Say — Easy
# https://leetcode.com/problems/count-and-say/
# Submission 2197382855 — Accepted, Python3
#
# My thinking: I start from "1" and build each next term
# by reading the previous one out loud — counting each run
# of equal digits and writing "how many, then which digit".

class Solution:
    def countAndSay(self, n: int) -> str:
        # Start from "1" and build each term by reading off the previous one.
        current = "1"
        for _ in range(n - 1):
            nxt = []
            i = 0
            while i < len(current):
                j = i
                while j < len(current) and current[j] == current[i]:
                    j += 1
                # j - i is how many times current[i] repeats in a row.
                nxt.append(str(j - i))
                nxt.append(current[i])
                i = j
            current = "".join(nxt)
        return current
