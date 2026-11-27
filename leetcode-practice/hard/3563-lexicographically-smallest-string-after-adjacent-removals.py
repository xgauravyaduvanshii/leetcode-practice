# LeetCode 3563. Lexicographically Smallest String After Adjacent Removals — Hard
# https://leetcode.com/problems/lexicographically-smallest-string-after-adjacent-removals/
# Submission 2202848788 — Accepted, Python3


class Solution:
    def lexicographicallySmallestString(self, s: str) -> str:
        # My thinking: I work on intervals. can[i][j] says whether
        # s[i..j] can vanish completely — either it splits into two
        # vanishing halves, or its first character pairs with some
        # later consecutive character after the middle vanishes.
        # dp[i][j] is the smallest string obtainable from s[i..j]:
        # either keep s[i] and reduce the rest, or delete s[i]
        # together with a consecutive partner s[k] (the middle must
        # vanish first) and reduce what follows. Deleting can make
        # the result larger, so I keep the minimum of all options.
        n = len(s)

        def consec(a, b):
            d = abs(ord(a) - ord(b))
            return d == 1 or d == 25

        can = [[False] * n for _ in range(n)]
        dp = [[""] * n for _ in range(n)]
        for length in range(1, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if length % 2 == 0:
                    for m in range(i, j):
                        if can[i][m] and can[m + 1][j]:
                            can[i][j] = True
                            break
                    if not can[i][j]:
                        for k in range(i + 1, j + 1):
                            if consec(s[i], s[k]) and (k == i + 1 or can[i + 1][k - 1]) and (k == j or can[k + 1][j]):
                                can[i][j] = True
                                break
                best = s[i] + (dp[i + 1][j] if i + 1 <= j else "")
                for k in range(i + 1, j + 1):
                    if consec(s[i], s[k]) and (k == i + 1 or can[i + 1][k - 1]):
                        rest = dp[k + 1][j] if k + 1 <= j else ""
                        if rest < best:
                            best = rest
                dp[i][j] = best
        return dp[0][n - 1] if n else ""
