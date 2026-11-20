# 3168. Minimum Number of Chairs in a Waiting Room (Easy)
# https://leetcode.com/problems/minimum-number-of-chairs-in-a-waiting-room/
# Submission 2199983263 — Accepted, Python3
class Solution:
    def minimumChairs(self, s: str) -> int:
        # My thinking: walk through the events keeping
        # how many people are waiting right now. Every
        # entry adds one, every exit takes one away, and
        # the most people waiting at once is how many
        # chairs are needed.
        current = 0
        best = 0
        for ch in s:
            if ch == "E":
                current += 1
                best = max(best, current)
            else:
                current -= 1
        return best
