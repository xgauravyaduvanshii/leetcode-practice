import bisect


class Solution:
    def makeArrayIncreasing(self, arr1: list[int], arr2: list[int]) -> int:
        # My thinking: walk arr1 keeping, for each number of
        # swaps, the smallest last value reachable — a swap
        # always takes the tiniest arr2 value that still fits.
        arr2 = sorted(set(arr2))
        dp = {0: -1}
        for value in arr1:
            new_dp = {}
            for ops, last in dp.items():
                if value > last:
                    if ops not in new_dp or value < new_dp[ops]:
                        new_dp[ops] = value
                i = bisect.bisect_right(arr2, last)
                if i < len(arr2):
                    replacement = arr2[i]
                    if ops + 1 not in new_dp or replacement < new_dp[ops + 1]:
                        new_dp[ops + 1] = replacement
            dp = new_dp
            if not dp:
                return -1
        return min(dp)
