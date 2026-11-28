# LeetCode 2434. Using a Robot to Print the Lexicographically Smallest String — Medium
# https://leetcode.com/problems/using-a-robot-to-print-the-lexicographically-smallest-string/
# Submission 2204943639 — Accepted, Python3
#
# My thinking: count the letters still left in the string, push each
# letter onto a stack, and pop from the stack whenever its top is no
# larger than the smallest letter still to come. That prints the
# smallest available letter as early as possible, which is exactly
# what makes the result lexicographically smallest.
class Solution:
    def robotWithString(self, s: str) -> str:
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - 97] += 1
        smallest = 0
        stack = []
        res = []
        for ch in s:
            stack.append(ch)
            freq[ord(ch) - 97] -= 1
            while smallest < 26 and freq[smallest] == 0:
                smallest += 1
            while stack and (smallest == 26 or ord(stack[-1]) - 97 <= smallest):
                res.append(stack.pop())
        return "".join(res)
