# LeetCode 2454. Next Greater Element IV — Hard
# https://leetcode.com/problems/next-greater-element-iv/
# Submission 2201751521 — Accepted, Python3
#
# My thinking: the second greater is the
# first thing past the first greater that
# still beats me — I find the first
# greater with a plain monotonic stack,
# then ask a segment tree for the first
# spot after it whose value tops mine.
# (A two-stack shortcut looks tempting
# but it buries small waiters under a
# bigger one and skips their answer.)

class Solution:
    def secondGreaterElement(self, nums: list[int]) -> list[int]:
        n = len(nums)
        nge = [-1] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()
            if stack:
                nge[i] = stack[-1]
            stack.append(i)
        size = 1
        while size < n:
            size *= 2
        tree = [0] * (2 * size)
        for i, x in enumerate(nums):
            tree[size + i] = x
        for i in range(size - 1, 0, -1):
            tree[i] = max(tree[2 * i], tree[2 * i + 1])

        def find_first(lo, hi, threshold):
            # leftmost index in [lo, hi] with value > threshold, else -1
            def rec(node, nl, nr):
                if nr < lo or nl > hi or tree[node] <= threshold:
                    return -1
                if nl == nr:
                    return nl
                mid = (nl + nr) // 2
                left = rec(2 * node, nl, mid)
                if left != -1:
                    return left
                return rec(2 * node + 1, mid + 1, nr)
            return rec(1, 0, size - 1)

        ans = [-1] * n
        for i in range(n):
            j = nge[i]
            if j == -1:
                continue
            k = find_first(j + 1, n - 1, nums[i])
            if k != -1:
                ans[i] = nums[k]
        return ans
