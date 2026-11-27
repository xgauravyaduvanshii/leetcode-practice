class Solution:
    def minimumMountainRemovals(self, nums: list[int]) -> int:
        # My thinking: a mountain is a climb then a fall, so
        # measure the longest climb ending at each point and
        # the longest fall starting there, then join the best
        # pair at a peak.
        n = len(nums)
        left = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    left[i] = max(left[i], left[j] + 1)
        right = [1] * n
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if nums[j] < nums[i]:
                    right[i] = max(right[i], right[j] + 1)
        best = 0
        for i in range(n):
            if left[i] > 1 and right[i] > 1:
                best = max(best, left[i] + right[i] - 1)
        return n - best
