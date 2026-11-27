# LeetCode 2380. Time Needed to Rearrange a Binary String — Medium
# https://leetcode.com/problems/time-needed-to-rearrange-a-binary-string/
# Submission 2204768465 — Accepted, Python3
#
# My thinking: in one second every "01" becomes "10", so a '1' moves
# right past zeros one step per second. For each '1', count the zeros
# before it: it needs at least that many seconds to pass them all, and
# each '1' also waits one second after the previous '1' moves (they
# cannot overtake). The answer is the max over all '1's of
# max(previous seconds + 1, zeros before it).
class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        seconds = 0
        zeros = 0
        for ch in s:
            if ch == '0':
                zeros += 1
            elif zeros > 0:
                seconds = max(seconds + 1, zeros)
        return seconds
