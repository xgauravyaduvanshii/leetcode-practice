# LeetCode 3337. Total Characters in String After Transformations II — Hard
# https://leetcode.com/problems/total-characters-in-string-after-transformations-ii/
# Submission 2202390004 — Accepted, Python3
from typing import List

MOD = 10 ** 9 + 7


class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        # My thinking: only the counts of each letter matter. One
        # transformation maps letter i to one copy each of the next nums[i]
        # letters, which is a 26x26 transition matrix. I raise that matrix
        # to the t-th power by binary exponentiation and apply it to the
        # initial count vector; the answer is the total count afterwards.
        # A row sum of the powered matrix is the number of descendants of
        # one letter after t transformations.
        n = 26
        mat = [[0] * n for _ in range(n)]
        for i in range(n):
            for d in range(1, nums[i] + 1):
                mat[i][(i + d) % n] += 1

        def mat_mult(A, B):
            C = [[0] * n for _ in range(n)]
            for i in range(n):
                Ai = A[i]
                Ci = C[i]
                for k in range(n):
                    aik = Ai[k]
                    if aik:
                        Bk = B[k]
                        for j in range(n):
                            Ci[j] = (Ci[j] + aik * Bk[j]) % MOD
            return C

        power = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
        base = mat
        e = t
        while e:
            if e & 1:
                power = mat_mult(power, base)
            base = mat_mult(base, base)
            e >>= 1
        cnt = [0] * n
        for ch in s:
            cnt[ord(ch) - 97] += 1
        ans = 0
        for i in range(n):
            if cnt[i]:
                ans = (ans + cnt[i] * sum(power[i])) % MOD
        return ans
