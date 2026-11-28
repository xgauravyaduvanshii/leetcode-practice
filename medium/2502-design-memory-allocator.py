# LeetCode 2502. Design Memory Allocator — Medium
# https://leetcode.com/problems/design-memory-allocator/
# Submission 2204977285 — Accepted, Python3
#
# My thinking: keep the memory as an array holding the owner id of
# each block (0 means free). Allocate scans for the first free run
# of the requested size and stamps it with the id; free clears every
# block owned by the id and counts them.
class Allocator:
    def __init__(self, n: int):
        self.mem = [0] * n

    def allocate(self, size: int, mID: int) -> int:
        n = len(self.mem)
        count = 0
        start = 0
        for i in range(n):
            if self.mem[i] == 0:
                if count == 0:
                    start = i
                count += 1
                if count == size:
                    for j in range(start, start + size):
                        self.mem[j] = mID
                    return start
            else:
                count = 0
        return -1

    def freeMemory(self, mID: int) -> int:
        count = 0
        for i in range(len(self.mem)):
            if self.mem[i] == mID:
                self.mem[i] = 0
                count += 1
        return count
