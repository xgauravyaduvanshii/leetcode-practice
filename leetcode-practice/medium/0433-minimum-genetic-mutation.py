# LeetCode 433. Minimum Genetic Mutation — Medium
# https://leetcode.com/problems/minimum-genetic-mutation/
# Submission 2198792994 — Accepted, Python3
#
# My thinking: every gene is a node and two genes
# are joined when they differ in exactly one letter.
# A breadth-first search from the start gene finds
# the fewest mutations to the target — each step
# tries all four letters in every position.

from collections import deque


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        bank = set(bank)
        if endGene not in bank:
            return -1
        queue = deque([(startGene, 0)])
        seen = {startGene}
        while queue:
            gene, steps = queue.popleft()
            if gene == endGene:
                return steps
            for i in range(len(gene)):
                for base in "ACGT":
                    mutated = gene[:i] + base + gene[i + 1:]
                    if mutated in bank and mutated not in seen:
                        seen.add(mutated)
                        queue.append((mutated, steps + 1))
        return -1
