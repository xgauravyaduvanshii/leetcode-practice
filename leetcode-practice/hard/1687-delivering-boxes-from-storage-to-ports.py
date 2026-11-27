# LeetCode 1687. Delivering Boxes from Storage to Ports — Hard
# https://leetcode.com/problems/delivering-boxes-from-storage-to-ports/
# Submission 2201091956 — Accepted, Python3
#
# My thinking: a trip carries boxes in order, so the
# split points are all that matter — I keep the cheapest
# cost to reach each split with a sliding window that
# respects the weight limit and a queue that always
# hands me the best split inside it.

from collections import deque

class Solution:
    def boxDelivering(self, boxes: list[list[int]], portsCount: int, maxBoxes: int, maxWeight: int) -> int:
        n = len(boxes)
        pref = [0] * n
        for i in range(1, n):
            pref[i] = pref[i - 1] + (1 if boxes[i][0] != boxes[i - 1][0] else 0)
        dp = [0] * (n + 1)
        wsum = [0] * (n + 1)
        for i in range(n):
            wsum[i + 1] = wsum[i] + boxes[i][1]
        queue = deque([0])
        left = 0
        for i in range(1, n + 1):
            while i - left > maxBoxes or wsum[i] - wsum[left] > maxWeight:
                if queue[0] == left:
                    queue.popleft()
                left += 1
            dp[i] = dp[queue[0]] + pref[i - 1] - pref[queue[0]] + 2
            if i < n:
                while queue and dp[queue[-1]] - pref[queue[-1]] >= dp[i] - pref[i]:
                    queue.pop()
                queue.append(i)
        return dp[n]
