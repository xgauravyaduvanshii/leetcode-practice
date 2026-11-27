class Solution:
    def maxSumOfThreeSubarrays(self, nums: list[int], k: int) -> list[int]:
        # My thinking: for each middle window, pair it with the best
        # window on its left and the best on its right — precompute
        # both bests once, then scan the middles.
        n = len(nums)
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)

        def window_sum(i):
            return prefix[i + k] - prefix[i]

        # best_left[i] = start of the best window in [0, i]
        best_left = [0] * n
        best = 0
        for i in range(n - k + 1):
            if window_sum(i) > window_sum(best):
                best = i
            best_left[i] = best
        # best_right[i] = start of the best window in [i, n - k]
        best_right = [0] * n
        best = n - k
        for i in range(n - k, -1, -1):
            if window_sum(i) >= window_sum(best):
                best = i
            best_right[i] = best
        answer = [-1, -1, -1]
        best_total = -1
        for mid in range(k, n - 2 * k + 1):
            left = best_left[mid - k]
            right = best_right[mid + k]
            total = window_sum(left) + window_sum(mid) + window_sum(right)
            if total > best_total:
                best_total = total
                answer = [left, mid, right]
        return answer
