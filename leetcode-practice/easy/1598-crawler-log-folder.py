# LeetCode 1598. Crawler Log Folder — Easy
# https://leetcode.com/problems/crawler-log-folder/
# Submission 2197588646 — Accepted, Python3
#
# My thinking: I track how deep I am in the folders.
# A folder name takes me one level deeper, "../"
# takes me one level up (but never above the root),
# and "./" does nothing. The final depth is the
# number of steps back to the main folder.

class Solution:
    def minOperations(self, logs: list[str]) -> int:
        depth = 0
        for log in logs:
            if log == "../":
                depth = max(0, depth - 1)
            elif log == "./":
                pass
            else:
                depth += 1
        return depth
