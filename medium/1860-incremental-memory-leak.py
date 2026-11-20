# 1860. Incremental Memory Leak (Medium)
# https://leetcode.com/problems/incremental-memory-leak/
# Submission 2199950935 — Accepted, Python3
from typing import List


class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        # My thinking: just play the leak out second by
        # second. At second t the bigger memory gives up
        # t units (ties go to memory1). The moment neither
        # memory holds t units, the program crashes, and
        # t is the crash second.
        second = 1
        while second <= max(memory1, memory2):
            if memory1 >= memory2:
                memory1 -= second
            else:
                memory2 -= second
            second += 1
        return [second, memory1, memory2]
