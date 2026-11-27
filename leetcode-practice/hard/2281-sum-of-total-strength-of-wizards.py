# LeetCode 2281. Sum of Total Strength of Wizards — Hard
# https://leetcode.com/problems/sum-of-total-strength-of-wizards/
# Submission 2201653839 — Accepted, Python3
#
# My thinking: every subarray has one
# weakest wizard, so I hand each wizard the
# stretches where it is the weakest and
# add its strength times every subarray
# sum those stretches hold.

class Solution:
    def totalStrength(self, strength: list[int]) -> int:
        MOD = 10 ** 9 + 7
        n = len(strength)
        pref = [0] * (n + 1)
        for i, x in enumerate(strength):
            pref[i + 1] = (pref[i] + x) % MOD
        pref_pref = [0] * (n + 2)
        for i in range(n + 1):
            pref_pref[i + 1] = (pref_pref[i] + pref[i]) % MOD
        left = [-1] * n
        stack = []
        for i, x in enumerate(strength):
            while stack and strength[stack[-1]] >= x:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)
        right = [n] * n
        stack = []
        for i in range(n - 1, -1, -1):
            x = strength[i]
            while stack and strength[stack[-1]] > x:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)
        ans = 0
        for i, x in enumerate(strength):
            L = left[i] + 1
            R = right[i] - 1
            left_count = i - L + 1
            right_count = R - i + 1
            sum_right = (pref_pref[R + 2] - pref_pref[i + 1]) % MOD
            sum_left = (pref_pref[i + 1] - pref_pref[L]) % MOD
            sub_sum = (left_count * sum_right - right_count * sum_left) % MOD
            ans = (ans + x * sub_sum) % MOD
        return ans
