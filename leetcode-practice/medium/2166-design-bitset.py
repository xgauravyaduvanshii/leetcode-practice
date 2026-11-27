# LeetCode 2166. Design Bitset — Medium
# https://leetcode.com/problems/design-bitset/
# Submission 2204483953 — Accepted, Python3
#
# My thinking: flipping every bit one by one would be slow, so I keep
# a single flipped flag and store the bits as written: the real value of
# a bit is its stored value XOR the flag. fix and unfix then only touch
# one stored bit and adjust the count of ones, flip just toggles the
# flag and mirrors the count, and toString renders each bit through the
# flag.
class Bitset:
    def __init__(self, size: int):
        self.size = size
        self.bits = [0] * size
        self.flipped = False
        self.ones = 0

    def fix(self, idx: int) -> None:
        actual = self.bits[idx] ^ (1 if self.flipped else 0)
        if actual == 0:
            self.bits[idx] ^= 1
            self.ones += 1

    def unfix(self, idx: int) -> None:
        actual = self.bits[idx] ^ (1 if self.flipped else 0)
        if actual == 1:
            self.bits[idx] ^= 1
            self.ones -= 1

    def flip(self) -> None:
        self.flipped = not self.flipped
        self.ones = self.size - self.ones

    def all(self) -> bool:
        return self.ones == self.size

    def one(self) -> bool:
        return self.ones > 0

    def count(self) -> int:
        return self.ones

    def toString(self) -> str:
        if self.flipped:
            return ''.join('1' if b == 0 else '0' for b in self.bits)
        return ''.join(str(b) for b in self.bits)
