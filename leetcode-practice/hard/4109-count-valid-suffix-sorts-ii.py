# LeetCode 4109. Count Valid Suffix Sorts II — Hard
# https://leetcode.com/problems/count-valid-suffix-sorts-ii/
# Submission 2203736970 — Accepted, Python3
class Solution:
    def countSuffix(self, nums: list[int], target: list[int]) -> list[int]:
        # My thinking: sorting a suffix nums[i..] in
        # non-increasing order only rearranges the
        # multiset, so a window target[k..k+n-1] can
        # match only when it holds exactly the same
        # values as nums. Slide a frequency-difference
        # count over target and keep a "bad" tally of
        # values whose counts disagree; bad == 0 means
        # the window is a multiset match. For such a
        # window, a suffix sort starting at i keeps the
        # prefix nums[0..i-1] untouched and sorts the
        # rest, so the result must agree with target
        # on that prefix: i can be at most p, the
        # matching-prefix length, found for every k by
        # one Z-function run on nums + [0] + target.
        # The sorted suffix is non-increasing, so the
        # window must be non-increasing from i on:
        # i must lie after the last adjacent increase
        # in the window (tracked by last_inc), giving
        # a lower bound q. The valid i are then
        # q..min(p, n-1), counted per window.
        n = len(nums)
        m = len(target)
        s = nums + [0] + target
        N = len(s)
        z = [0] * N
        l = r = 0
        for i in range(1, N):
            if i <= r:
                z[i] = min(r - i + 1, z[i - l])
            while i + z[i] < N and s[z[i]] == s[i + z[i]]:
                z[i] += 1
            if i + z[i] - 1 > r:
                l, r = i, i + z[i] - 1
        last_inc = [-1] * m
        cur = -1
        for j in range(m - 1):
            if target[j] < target[j + 1]:
                cur = j
            last_inc[j] = cur
        last_inc[m - 1] = cur
        diff = [0] * 100001
        for v in nums:
            diff[v] += 1
        for j in range(n):
            diff[target[j]] -= 1
        bad = 0
        for d in diff:
            if d:
                bad += 1
        ans = [0] * (m - n + 1)
        for k in range(m - n + 1):
            if k:
                v = target[k - 1]
                if diff[v] == 0:
                    bad += 1
                diff[v] += 1
                if diff[v] == 0:
                    bad -= 1
                v = target[k + n - 1]
                if diff[v] == 0:
                    bad += 1
                diff[v] -= 1
                if diff[v] == 0:
                    bad -= 1
            if bad == 0:
                p = z[n + 1 + k]
                if p > n:
                    p = n
                j = last_inc[k + n - 2] if n >= 2 else -1
                q = 0 if j < k else j + 1 - k
                hi = p if p < n - 1 else n - 1
                cnt = hi - q + 1
                if cnt > 0:
                    ans[k] = cnt
        return ans
