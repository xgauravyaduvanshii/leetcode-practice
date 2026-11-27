# LeetCode 3519. Count Numbers with Non-Decreasing Digits — Hard
# https://leetcode.com/problems/count-numbers-with-non-decreasing-digits/
# Submission 2202798350 — Accepted, Python3
from functools import lru_cache

MOD = 10 ** 9 + 7


class Solution:
    def countNumbers(self, l: str, r: str, b: int) -> int:
        # My thinking: l and r are decimal strings that can be 100
        # digits long, so I convert the bound to base b by repeated
        # decimal-string division, then run a digit DP over those
        # base-b digits: at each position I choose the next digit no
        # smaller than the previous one (leading zeros do not count as
        # started), and the answer is count(r) minus count(l - 1).
        def divmod_str(s, b):
            q = []
            rem = 0
            for ch in s:
                cur = rem * 10 + int(ch)
                q.append(str(cur // b))
                rem = cur % b
            qs = "".join(q).lstrip("0") or "0"
            return qs, rem

        def to_base_b(dec_str):
            if dec_str == "0":
                return [0]
            digits = []
            s = dec_str
            while s != "0":
                s, rem = divmod_str(s, b)
                digits.append(rem)
            return digits[::-1]

        def dec_minus_one(s):
            digits = list(s)
            i = len(digits) - 1
            while digits[i] == "0":
                digits[i] = "9"
                i -= 1
            digits[i] = str(int(digits[i]) - 1)
            res = "".join(digits).lstrip("0")
            return res if res else "0"

        def count_leq(dec_str):
            digits = to_base_b(dec_str)
            L = len(digits)

            @lru_cache(maxsize=None)
            def dp(pos, prev, tight, started):
                if pos == L:
                    return 1
                limit = digits[pos] if tight else b - 1
                total = 0
                for d in range(limit + 1):
                    ntight = tight and (d == digits[pos])
                    if not started and d == 0:
                        total = (total + dp(pos + 1, prev, ntight, False)) % MOD
                    elif not started:
                        total = (total + dp(pos + 1, d, ntight, True)) % MOD
                    elif d >= prev:
                        total = (total + dp(pos + 1, d, ntight, True)) % MOD
                return total

            return dp(0, 0, True, False)

        res = count_leq(r)
        if l != "0":
            res = (res - count_leq(dec_minus_one(l))) % MOD
        return res
