# LeetCode 3782. Last Remaining Integer After Alternating Deletion Operations — Hard
# https://leetcode.com/problems/last-remaining-integer-after-alternating-deletion-operations/
# Submission 2203175322 — Accepted, Python3


class Solution:
    def lastInteger(self, n: int) -> int:
        # My thinking: the survivors always form an arithmetic
        # sequence, so I only track its first element (head),
        # its step, and how many remain. A left-to-right pass
        # keeps the odd positions, so the head never moves; a
        # right-to-left pass keeps the odd positions from the
        # right, which moves the head forward by one step
        # exactly when the count is even. Either way the count
        # halves (rounding up) and the step doubles, and the
        # passes alternate until one number is left.
        head = 1
        step = 1
        remaining = n
        left = True
        while remaining > 1:
            if not left and remaining % 2 == 0:
                head += step
            remaining = (remaining + 1) // 2
            step *= 2
            left = not left
        return head
