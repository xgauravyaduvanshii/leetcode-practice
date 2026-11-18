# LeetCode 753. Cracking the Safe — Hard
# https://leetcode.com/problems/cracking-the-safe/
# Submission 2198673055 — Accepted, Python3
#
# My thinking: the answer is a De Bruijn sequence — an
# Eulerian walk over (n-1)-digit nodes where each edge
# adds one digit. I walk it with an iterative
# Hierholzer, writing each digit down when its edge
# finishes. The digits come out in the right order as
# they are — reversing them was the bug in my first
# try, it repeated 000 and missed 001.

class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        start = "0" * (n - 1)
        seen = set()
        answer = []
        stack = [(start, 0, "")]
        while stack:
            node, next_digit, incoming = stack[-1]
            if next_digit < k:
                stack[-1] = (node, next_digit + 1, incoming)
                edge = node + str(next_digit)
                if edge not in seen:
                    seen.add(edge)
                    stack.append((edge[1:], 0, str(next_digit)))
            else:
                stack.pop()
                if incoming:
                    answer.append(incoming)
        return "".join(answer) + "0" * (n - 1)
