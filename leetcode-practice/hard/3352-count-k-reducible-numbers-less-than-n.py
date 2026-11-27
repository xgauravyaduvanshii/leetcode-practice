# LeetCode 3352. Count K-Reducible Numbers Less Than N — Hard
# https://leetcode.com/problems/count-k-reducible-numbers-less-than-n/
# Submission 2202415395 — Accepted, Python3
MOD = 10 ** 9 + 7


class Solution:
    def countKReducible(self, s: str, k: int) -> int:
        # My thinking: one operation replaces x by its popcount, so after
        # the first operation the value is at most len(s), and the remaining
        # steps depend only on the popcount. I precompute steps[c], the
        # operations needed to reduce c to 1, then count binary strings
        # below s by popcount with a digit DP: at each '1' in s I count the
        # completions with a smaller bit here, using binomial coefficients.
        # A number is k-reducible exactly when steps[popcount] <= k - 1.
        L = len(s)
        steps = [0] * (L + 1)
        for c in range(2, L + 1):
            steps[c] = 1 + steps[bin(c).count('1')]
        C = [[0] * (L + 1) for _ in range(L + 1)]
        for i in range(L + 1):
            C[i][0] = C[i][i] = 1
            for j in range(1, i):
                C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % MOD
        ans = 0
        ones = 0
        for i, ch in enumerate(s):
            if ch == '1':
                rem = L - 1 - i
                for c in range(rem + 1):
                    pc = ones + c
                    if pc >= 1 and steps[pc] <= k - 1:
                        ans = (ans + C[rem][c]) % MOD
                ones += 1
        return ans
