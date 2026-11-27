# LeetCode 3463. Check If Digits Are Equal in String After Operations II — Hard
# https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-ii/
# Submission 2202557387 — Accepted 684/684, Python3
from typing import List


class Solution:
    def hasSameDigits(self, s: str) -> bool:
        # My thinking: each reduction is a Pascal-triangle
        # weighting, so after n - 2 rounds the two final digits
        # are sums of C(n-2, i) * s[i] and C(n-2, i) * s[i+1]
        # modulo 10. I get each binomial coefficient mod 10
        # with Lucas' theorem mod 2 and mod 5, combined by
        # the Chinese remainder theorem (10 is not prime, so
        # no direct modular inverse exists).
        n = len(s)
        digits = [ord(ch) - 48 for ch in s]

        # Small binomial coefficients C(a, b) for a, b < 5.
        small = [[0] * 5 for _ in range(5)]
        for a in range(5):
            small[a][0] = small[a][a] = 1
            for b in range(1, a):
                small[a][b] = small[a - 1][b - 1] + small[a - 1][b]

        def binom_mod_10(N: int, K: int) -> int:
            if K < 0 or K > N:
                return 0
            # Mod 2: C(N, K) is odd exactly when K's set bits
            # are a subset of N's (Lucas in base 2).
            r2 = 1 if (K & ~N) == 0 else 0
            # Mod 5: Lucas in base 5.
            r5 = 1
            nn, kk = N, K
            while nn > 0 or kk > 0:
                ni, ki = nn % 5, kk % 5
                if ki > ni:
                    r5 = 0
                    break
                r5 = (r5 * small[ni][ki]) % 5
                nn //= 5
                kk //= 5
            # CRT: the number mod 10 is r5 or r5 + 5, whichever
            # has parity r2.
            return r5 if r5 % 2 == r2 else r5 + 5

        k = n - 2
        first = 0
        second = 0
        for i in range(n - 1):
            c = binom_mod_10(k, i)
            first = (first + c * digits[i]) % 10
            second = (second + c * digits[i + 1]) % 10
        return first == second
