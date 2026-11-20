class Solution:
    def minNumberOfSemesters(self, n: int, relations: list[list[int]], k: int) -> int:
        # My thinking: a semester is a set of courses whose
        # prerequisites are already done — so track which
        # courses are done as a bitmask and try every
        # affordable batch of the newly available ones.
        prereq = [0] * n
        for prev, nxt in relations:
            prereq[nxt - 1] |= 1 << (prev - 1)
        INF = float("inf")
        dp = [INF] * (1 << n)
        dp[0] = 0
        for mask in range(1 << n):
            avail = 0
            for i in range(n):
                if not mask & (1 << i) and (prereq[i] & ~mask) == 0:
                    avail |= 1 << i
            if avail == 0:
                continue
            if bin(avail).count("1") <= k:
                dp[mask | avail] = min(dp[mask | avail], dp[mask] + 1)
                continue
            sub = avail
            while sub:
                if bin(sub).count("1") <= k:
                    dp[mask | sub] = min(dp[mask | sub], dp[mask] + 1)
                sub = (sub - 1) & avail
        return dp[(1 << n) - 1]
