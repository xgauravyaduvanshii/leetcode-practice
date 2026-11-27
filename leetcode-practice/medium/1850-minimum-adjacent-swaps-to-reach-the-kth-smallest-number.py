# LeetCode 1850. Minimum Adjacent Swaps to Reach the Kth Smallest Number — Medium
# https://leetcode.com/problems/minimum-adjacent-swaps-to-reach-the-kth-smallest-number/
# Submission 2199947287 — Accepted, Python3
#
# My thinking: I walk the number forward k
# next-permutations, then count how many
# adjacent swaps turn the original into that
# target — pulling each needed digit left to
# its place, one swap at a time.

class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        digits = list(num)
        for _ in range(k):
            i = len(digits) - 2
            while i >= 0 and digits[i] >= digits[i + 1]:
                i -= 1
            j = len(digits) - 1
            while digits[j] <= digits[i]:
                j -= 1
            digits[i], digits[j] = digits[j], digits[i]
            digits[i + 1:] = reversed(digits[i + 1:])
        target = "".join(digits)
        swaps = 0
        current = list(num)
        for i in range(len(target)):
            if current[i] != target[i]:
                j = current.index(target[i], i)
                while j > i:
                    current[j], current[j - 1] = current[j - 1], current[j]
                    swaps += 1
                    j -= 1
        return swaps
