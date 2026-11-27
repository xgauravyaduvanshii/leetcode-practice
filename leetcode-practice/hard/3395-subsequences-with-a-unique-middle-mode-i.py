# LeetCode 3395. Subsequences with a Unique Middle Mode I — Hard
# https://leetcode.com/problems/subsequences-with-a-unique-middle-mode-i/
# Submission 2202502626 — Accepted 947/947, Python3
from typing import List


class Solution:
    def subsequencesWithMiddleMode(self, nums: List[int]) -> int:
        # My thinking: fix the middle index. Its value v is the unique
        # mode exactly when it occurs more often than any other value in
        # the five chosen spots. With x of the four other spots equal to v
        # the middle value occurs 1 + x times, so x = 0 can never work, x
        # >= 2 always works, and x = 1 works only when the three remaining
        # values are all different from each other. I count the x >= 2
        # choices by subtracting the x = 0 and x = 1 choices from all
        # choices, and the x = 1 choices with distinct others by counting
        # pairs on the far side whose two values differ and neither equals
        # the near side's value.
        MOD = 10 ** 9 + 7

        def c2(n):
            return n * (n - 1) // 2 if n >= 2 else 0

        n = len(nums)
        before = {}
        after = {}
        for v in nums:
            after[v] = after.get(v, 0) + 1
        ans = 0
        for m in range(n):
            v = nums[m]
            after[v] -= 1
            if after[v] == 0:
                del after[v]
            left = m
            right = n - 1 - m
            if left >= 2 and right >= 2:
                lv = before.get(v, 0)
                rv = after.get(v, 0)
                sb = left - lv
                sa = right - rv
                total = c2(left) * c2(right)
                xy0 = c2(sb) * c2(sa)
                xy1 = lv * sb * c2(sa) + c2(sb) * rv * sa
                ge2 = total - xy0 - xy1
                da = c2(sa) - sum(c2(c) for w, c in after.items() if w != v)
                db = c2(sb) - sum(c2(c) for w, c in before.items() if w != v)
                s_a = 0
                for w, cbw in before.items():
                    if w == v:
                        continue
                    caw = after.get(w, 0)
                    s_a += cbw * (da - caw * (sa - caw))
                s_b = 0
                for w, caw in after.items():
                    if w == v:
                        continue
                    cbw = before.get(w, 0)
                    s_b += caw * (db - cbw * (sb - cbw))
                ans = (ans + ge2 + lv * s_a + rv * s_b) % MOD
            before[v] = before.get(v, 0) + 1
        return ans
