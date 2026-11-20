class Solution:
    def countRangeSum(self, nums: list[int], lower: int, upper: int) -> int:
        # My thinking: a range sum is a difference of two prefix
        # sums, so count pairs of prefix sums whose difference falls
        # in [lower, upper] while merge-sorting them.
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)

        def sort_count(lo, hi):
            if hi - lo <= 1:
                return 0
            mid = (lo + hi) // 2
            count = sort_count(lo, mid) + sort_count(mid, hi)
            j = k = mid
            for i in range(lo, mid):
                while k < hi and prefix[k] - prefix[i] < lower:
                    k += 1
                while j < hi and prefix[j] - prefix[i] <= upper:
                    j += 1
                count += j - k
            prefix[lo:hi] = sorted(prefix[lo:hi])
            return count

        return sort_count(0, len(prefix))
