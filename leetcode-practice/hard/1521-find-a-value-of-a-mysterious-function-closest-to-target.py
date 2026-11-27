class Solution:
    def closestToTarget(self, arr: list[int], target: int) -> int:
        # My thinking: the AND of a subarray can only lose
        # bits as it grows — so keep the handful of distinct
        # values ending here and check each against the target.
        best = float("inf")
        cur = set()
        for x in arr:
            cur = {x & v for v in cur} | {x}
            for v in cur:
                best = min(best, abs(v - target))
        return best
