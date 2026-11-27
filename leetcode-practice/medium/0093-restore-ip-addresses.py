# LeetCode 93. Restore IP Addresses — Medium
# https://leetcode.com/problems/restore-ip-addresses/
# Submission 2200893394 — Accepted, Python3
#
# My thinking: I cut the string into four parts, one at a
# time — each part is one to three digits, cannot have a
# leading zero unless it is exactly "0", and must be at
# most 255.

class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        result = []

        def backtrack(start: int, parts: list[str]) -> None:
            if len(parts) == 4:
                if start == len(s):
                    result.append(".".join(parts))
                return
            for end in range(start + 1, min(start + 4, len(s) + 1)):
                part = s[start:end]
                if len(part) > 1 and part[0] == "0":
                    break
                if int(part) > 255:
                    break
                parts.append(part)
                backtrack(end, parts)
                parts.pop()

        backtrack(0, [])
        return result
