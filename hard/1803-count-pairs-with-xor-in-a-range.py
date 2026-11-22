# LeetCode 1803. Count Pairs With XOR in a Range — Hard
# https://leetcode.com/problems/count-pairs-with-xor-in-a-range/
# Submission 2201172224 — Accepted, Python3
#
# My thinking: pairs with xor below a limit are
# counted by walking a binary trie bit by bit —
# whenever the limit has a 1, the whole branch
# that keeps the xor's bit 0 counts at once. I
# take the count below high + 1 minus the count
# below low.

class Solution:
    def countPairs(self, nums: list[int], low: int, high: int) -> int:
        return self._count_less(nums, high + 1) - self._count_less(nums, low)

    def _count_less(self, nums, limit):
        # node: [child0, child1, count]
        trie = [[-1, -1, 0]]

        def insert(x):
            node = 0
            trie[node][2] += 1
            for b in range(15, -1, -1):
                bit = (x >> b) & 1
                if trie[node][bit] == -1:
                    trie[node][bit] = len(trie)
                    trie.append([-1, -1, 0])
                node = trie[node][bit]
                trie[node][2] += 1

        def query(x):
            node = 0
            total = 0
            for b in range(15, -1, -1):
                if node == -1:
                    break
                bit_x = (x >> b) & 1
                bit_l = (limit >> b) & 1
                if bit_l == 1:
                    child = trie[node][bit_x]
                    if child != -1:
                        total += trie[child][2]
                    node = trie[node][1 - bit_x]
                else:
                    node = trie[node][bit_x]
            return total

        total = 0
        for x in nums:
            total += query(x)
            insert(x)
        return total
