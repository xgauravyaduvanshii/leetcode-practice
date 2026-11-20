class Solution:
    def largestNumber(self, cost: list[int], target: int) -> str:
        # My thinking: for every cost, keep the longest number
        # reachable — longer beats larger digits — and build
        # each cost up from the cheaper ones.
        dp = [None] * (target + 1)
        dp[0] = ""
        for t in range(1, target + 1):
            best = None
            for d in range(1, 10):
                c = cost[d - 1]
                if t >= c and dp[t - c] is not None:
                    cand = dp[t - c] + str(d)
                    if best is None or len(cand) > len(best) or (len(cand) == len(best) and cand > best):
                        best = cand
            dp[t] = best
        return dp[target] if dp[target] is not None else "0"
