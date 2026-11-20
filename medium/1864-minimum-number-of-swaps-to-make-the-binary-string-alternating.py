# 1864. Minimum Number of Swaps to Make the Binary String Alternating (Medium)
# https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-binary-string-alternating/
# Submission 2199951457 — Accepted, Python3
class Solution:
    def minSwaps(self, s: str) -> int:
        # My thinking: only two alternating patterns can
        # ever work, one starting with 0 and one with 1.
        # Count how many positions disagree with each
        # pattern; every swap fixes two disagreements.
        # If the counts of 0s and 1s cannot fill a
        # pattern, the answer is -1.
        n = len(s)
        ones = s.count("1")
        zeros = n - ones

        def mismatches(start: int) -> int:
            bad = 0
            for i, ch in enumerate(s):
                want = str((start + i) % 2)
                if ch != want:
                    bad += 1
            return bad

        if n % 2 == 1:
            if abs(ones - zeros) != 1:
                return -1
            start = 1 if ones > zeros else 0
            return mismatches(start) // 2
        if ones != zeros:
            return -1
        return min(mismatches(0), mismatches(1)) // 2
