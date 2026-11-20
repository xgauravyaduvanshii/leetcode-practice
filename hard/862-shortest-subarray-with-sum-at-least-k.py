from collections import deque


class Solution:
    def shortestSubarray(self, nums: list[int], k: int) -> int:
        # My thinking: prefix sums turn a subarray sum into a
        # difference, and a monotone queue keeps only the prefix
        # sums that can still give the shortest answer.
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
        queue = deque()
        best = float("inf")
        for i, p in enumerate(prefix):
            while queue and prefix[queue[-1]] >= p:
                queue.pop()
            while queue and p - prefix[queue[0]] >= k:
                best = min(best, i - queue.popleft())
            queue.append(i)
        return -1 if best == float("inf") else best
