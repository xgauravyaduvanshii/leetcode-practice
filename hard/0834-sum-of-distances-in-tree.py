# LeetCode 834. Sum of Distances in Tree — Hard
# https://leetcode.com/problems/sum-of-distances-in-tree/
# Submission 2198680787 — Accepted, Python3
#
# My thinking: I root the tree and work bottom-up
# first — each node's answer is its children's
# answers plus one per node in their subtrees. Then I
# walk back down: moving the root across an edge
# shifts every node in that child's subtree one step
# closer and every other node one step farther.

from typing import List


class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        tree = [[] for _ in range(n)]
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        subtree_size = [1] * n
        answer = [0] * n

        def down(node, parent):
            for child in tree[node]:
                if child == parent:
                    continue
                down(child, node)
                subtree_size[node] += subtree_size[child]
                answer[node] += answer[child] + subtree_size[child]

        def up(node, parent):
            for child in tree[node]:
                if child == parent:
                    continue
                answer[child] = answer[node] + (n - 2 * subtree_size[child])
                up(child, node)

        down(0, -1)
        up(0, -1)
        return answer
