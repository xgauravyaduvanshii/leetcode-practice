# LeetCode 394. Decode String — Medium
# https://leetcode.com/problems/decode-string/
# Submission 2198773455 — Accepted, Python3
#
# My thinking: I scan the string once with a stack.
# A number builds up the repeat count, an opening
# bracket saves what I have so far, and a closing
# bracket repeats the inner piece and joins it back
# onto the saved part.

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current = ""
        count = 0
        for char in s:
            if char.isdigit():
                count = count * 10 + int(char)
            elif char == "[":
                stack.append((current, count))
                current = ""
                count = 0
            elif char == "]":
                previous, repeat = stack.pop()
                current = previous + current * repeat
            else:
                current += char
        return current
