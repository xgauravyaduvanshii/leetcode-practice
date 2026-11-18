# LeetCode 388. Longest Absolute File Path — Medium
# https://leetcode.com/problems/longest-absolute-file-path/
# Submission 2198768394 — Accepted, Python3
#
# My thinking: the tabs before a name give its
# depth. I keep the running path length at each
# depth — a directory adds its name plus one slash,
# a file (it has a dot) ends a path whose length I
# compare with the best so far.

class Solution:
    def lengthLongestPath(self, input: str) -> int:
        longest = 0
        depths = {0: 0}
        for line in input.split("\n"):
            depth = line.count("\t")
            name = line.replace("\t", "")
            if "." in name:
                longest = max(longest, depths[depth] + len(name))
            else:
                depths[depth + 1] = depths[depth] + len(name) + 1
        return longest
