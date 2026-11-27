# LeetCode 3614. Process String with Special Operations II — Hard
# https://leetcode.com/problems/process-string-with-special-operations-ii/
# Submission 2202873163 — Accepted, Python3


class Solution:
    def processStr(self, s: str, k: int) -> str:
        # My thinking: the result can grow to 10^15 characters, so
        # I never build it. I first record how long the result is
        # after each operation, capped above 10^15. Then I walk
        # backwards from the end: a letter answers the query when k
        # points at the position it appended, a '*' changes nothing,
        # a '#' maps k back into the first copy, and a '%' mirrors k
        # across the reversed string. If k is past the final length,
        # the answer is '.'.
        n = len(s)
        INF = 10 ** 18
        lens = []
        cur = 0
        for ch in s:
            if ch == '*':
                cur = max(0, cur - 1)
            elif ch == '#':
                cur = min(INF, cur * 2)
            elif ch == '%':
                pass
            else:
                cur = min(INF, cur + 1)
            lens.append(cur)
        if k >= lens[-1]:
            return '.'
        for i in range(n - 1, -1, -1):
            ch = s[i]
            prev_len = lens[i - 1] if i > 0 else 0
            if ch == '*':
                pass
            elif ch == '#':
                if prev_len > 0:
                    k %= prev_len
            elif ch == '%':
                k = prev_len - 1 - k
            else:
                if k == lens[i] - 1:
                    return ch
        return '.'
