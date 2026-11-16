# LeetCode 2325. Decode the Message — Easy
# https://leetcode.com/problems/decode-the-message/
# Submission 2197623138 — Accepted, Python3
#
# My thinking: I read the key from left to right and
# map each new letter I meet to a, b, c, and so on.
# Then I translate the message through that map,
# leaving spaces alone.

class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        mapping = {}
        nxt = ord('a')
        for ch in key:
            if ch != ' ' and ch not in mapping:
                mapping[ch] = chr(nxt)
                nxt += 1
        return ''.join(mapping[ch] if ch != ' ' else ' ' for ch in message)
