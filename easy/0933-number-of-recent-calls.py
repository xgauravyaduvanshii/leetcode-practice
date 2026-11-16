# LeetCode 933. Number of Recent Calls — Easy
# https://leetcode.com/problems/number-of-recent-calls/
# Submission 2197543445 — Accepted, Python3
#
# My thinking: I keep the call times in a queue. Each
# new call goes on the end, and I drop anything
# from the front that is older than 3000 ms. What
# is left in the queue is exactly the calls in
# the last 3000 ms.

from collections import deque


class RecentCounter:
    def __init__(self):
        self.q = deque()

    def ping(self, t: int) -> int:
        self.q.append(t)
        while self.q[0] < t - 3000:
            self.q.popleft()
        return len(self.q)
