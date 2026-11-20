# 4020. Elevator Requests I (Easy)
# https://leetcode.com/problems/elevator-requests-i/
# Submission 2200097832 — Accepted, Python3
class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        # My thinking: the lift starts at floor zero,
        # so the total time is just the distance it
        # travels between one request and the next.
        total = 0
        cur = 0
        for r in requests:
            total += abs(r - cur)
            cur = r
        return total
