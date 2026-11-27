# LeetCode 1960. Maximum Product of the Length of Two Palindromic Substrings — Hard
# https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-substrings/
# Submission 2201270718 — Accepted, Python3
#
# My thinking: Manacher gives me every
# palindrome's reach, and a sweep keeps the
# smallest centre that still reaches each end —
# that is the longest palindrome ending there.
# The same sweep from the right gives the longest
# starting there, and the best split is the best
# left length times the best right length.

import heapq

class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)
        d1 = [0] * n
        l = 0
        r = -1
        for i in range(n):
            k = 1 if i > r else min(d1[l + r - i], r - i + 1)
            while i - k >= 0 and i + k < n and s[i - k] == s[i + k]:
                k += 1
            d1[i] = k
            if i + k - 1 > r:
                l = i - k + 1
                r = i + k - 1
        d2 = [0] * n
        l = 0
        r = -1
        for i in range(n):
            k = 0 if i > r else min(d2[l + r - i + 1], r - i + 1)
            while i - k - 1 >= 0 and i + k < n and s[i - k - 1] == s[i + k]:
                k += 1
            d2[i] = k
            if i + k - 1 > r:
                l = i - k
                r = i + k - 1
        end_max = [0] * n
        heap = []
        for e in range(n):
            heapq.heappush(heap, (e, e + d1[e] - 1))
            while heap and heap[0][1] < e:
                heapq.heappop(heap)
            if heap:
                c = heap[0][0]
                end_max[e] = max(end_max[e], 2 * (e - c) + 1)
        heap = []
        for e in range(n):
            heapq.heappush(heap, (e, e + d2[e] - 1))
            while heap and heap[0][1] < e:
                heapq.heappop(heap)
            if heap:
                c = heap[0][0]
                end_max[e] = max(end_max[e], 2 * (e - c + 1))
        pre = [0] * n
        best = 0
        for e in range(n):
            best = max(best, end_max[e])
            pre[e] = best
        start_max = [0] * n
        heap = []
        for st in range(n - 1, -1, -1):
            heapq.heappush(heap, (-st, st - d1[st] + 1))
            while heap and heap[0][1] > st:
                heapq.heappop(heap)
            if heap:
                c = -heap[0][0]
                start_max[st] = max(start_max[st], 2 * (c - st) + 1)
        heap = []
        for st in range(n - 1, -1, -1):
            heapq.heappush(heap, (-st, st - d2[st]))
            while heap and heap[0][1] > st:
                heapq.heappop(heap)
            if heap:
                c = -heap[0][0]
                start_max[st] = max(start_max[st], 2 * (c - st))
        suf = [0] * n
        best = 0
        for st in range(n - 1, -1, -1):
            best = max(best, start_max[st])
            suf[st] = best
        ans = 0
        for i in range(n - 1):
            ans = max(ans, pre[i] * suf[i + 1])
        return ans
