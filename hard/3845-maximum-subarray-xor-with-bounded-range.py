# LeetCode 3845. Maximum Subarray XOR with Bounded Range — Hard
# https://leetcode.com/problems/maximum-subarray-xor-with-bounded-range/
# Submission 2203288193 — Accepted, Python3
from collections import deque


class Solution:
    def maxXor(self, nums: list[int], k: int) -> int:
        # My thinking: the xor of a subarray nums[l..r] is
        # pref[r+1] ^ pref[l], so for each right end r I need
        # the prefix xor in the window that maximises the xor
        # with pref[r+1] — a binary trie over the 15 bits
        # answers that, and it supports deleting a prefix xor
        # when it leaves the window. The window itself is the
        # longest stretch ending at r whose max minus min is
        # at most k: two monotone deques track the min and max
        # while the left edge only moves forward, because
        # shrinking a subarray can only shrink max minus min.
        n = len(nums)
        pref = [0] * (n + 1)
        for i, v in enumerate(nums):
            pref[i + 1] = pref[i] ^ v
        child = [[-1, -1]]
        cnt = [0]

        def trie_add(x, delta):
            node = 0
            cnt[node] += delta
            for b in range(14, -1, -1):
                bit = (x >> b) & 1
                if child[node][bit] == -1:
                    child[node][bit] = len(child)
                    child.append([-1, -1])
                    cnt.append(0)
                node = child[node][bit]
                cnt[node] += delta

        def trie_best(x):
            node = 0
            ans = 0
            for b in range(14, -1, -1):
                bit = (x >> b) & 1
                want = bit ^ 1
                nxt = child[node][want]
                if nxt != -1 and cnt[nxt] > 0:
                    ans |= 1 << b
                    node = nxt
                else:
                    node = child[node][bit]
            return ans

        trie_add(pref[0], 1)
        min_d, max_d = deque(), deque()
        left = 0
        ans = 0
        for r in range(n):
            while max_d and nums[max_d[-1]] <= nums[r]:
                max_d.pop()
            max_d.append(r)
            while min_d and nums[min_d[-1]] >= nums[r]:
                min_d.pop()
            min_d.append(r)
            while nums[max_d[0]] - nums[min_d[0]] > k:
                if max_d[0] == left:
                    max_d.popleft()
                if min_d[0] == left:
                    min_d.popleft()
                trie_add(pref[left], -1)
                left += 1
            if r > 0:
                trie_add(pref[r], 1)
            ans = max(ans, trie_best(pref[r + 1]))
        return ans
