# LeetCode 1629. Slowest Key — Easy
# https://leetcode.com/problems/slowest-key/
# Submission 2197590657 — Accepted, Python3
#
# My thinking: the duration of each key press is the
# gap between its release time and the previous
# one. I keep the longest duration I have seen —
# ties go to the lexicographically larger key.

class Solution:
    def slowestKey(self, releaseTimes: list[int], keysPressed: str) -> str:
        best_key = keysPressed[0]
        best_duration = releaseTimes[0]
        for i in range(1, len(keysPressed)):
            duration = releaseTimes[i] - releaseTimes[i - 1]
            if duration > best_duration or (duration == best_duration and keysPressed[i] > best_key):
                best_duration = duration
                best_key = keysPressed[i]
        return best_key
