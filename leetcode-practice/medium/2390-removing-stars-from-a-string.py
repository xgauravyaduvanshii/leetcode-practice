# LeetCode 2390. Removing Stars From a String — Medium
# https://leetcode.com/problems/removing-stars-from-a-string/
# Submission 2197777343 — Accepted, Python3
#
# My thinking: a star deletes the character right
# before it. I use a stack: push letters, and pop
# the top one whenever I see a star.

class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch == '*':
                stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)
