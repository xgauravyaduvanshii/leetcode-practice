# LeetCode 1717. Maximum Score From Removing Substrings — Medium
# https://leetcode.com/problems/maximum-score-from-removing-substrings/
# Submission 2199920010 — Accepted, Python3
#
# My thinking: removing the higher-value pair
# first can only help, so I take all of those
# with a stack, then sweep up the other pair
# from what is left.

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_pair(text, first, second, points):
            stack = []
            score = 0
            for ch in text:
                if stack and stack[-1] == first and ch == second:
                    stack.pop()
                    score += points
                else:
                    stack.append(ch)
            return "".join(stack), score

        if x >= y:
            s, score = remove_pair(s, "a", "b", x)
            _, extra = remove_pair(s, "b", "a", y)
        else:
            s, score = remove_pair(s, "b", "a", y)
            _, extra = remove_pair(s, "a", "b", x)
        return score + extra
