# LeetCode 1773. Count Items Matching a Rule — Easy
# https://leetcode.com/problems/count-items-matching-a-rule/
# Submission 2197597654 — Accepted, Python3
#
# My thinking: each item is [type, color, name], so
# the rule key just picks which position to look
# at. I map the key to its index and count the
# items whose value there matches.

class Solution:
    def countMatches(self, items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
        idx = {"type": 0, "color": 1, "name": 2}[ruleKey]
        return sum(1 for item in items if item[idx] == ruleValue)
