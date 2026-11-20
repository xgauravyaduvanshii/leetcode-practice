# 762. Prime Number of Set Bits in Binary Representation (Easy)
# https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/
# Submission 2199964231 — Accepted, Python3
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        # My thinking: numbers up to a million have at
        # most 20 set bits, and the primes among them are
        # only 2, 3, 5, 7, 11, 13, 17 and 19. So for each
        # number in the range I count its set bits and
        # check the count against that small set.
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        total = 0
        for num in range(left, right + 1):
            if bin(num).count("1") in primes:
                total += 1
        return total
