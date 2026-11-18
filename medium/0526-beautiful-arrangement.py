# LeetCode 526. Beautiful Arrangement — Medium
# https://leetcode.com/problems/beautiful-arrangement/
# Submission 2198848465 — Accepted, Python3
#
# My thinking: I fill the positions one by one,
# trying each unused number that divides or is
# divisible by its position. Counting every
# complete placement gives the answer.

class Solution:
    def countArrangement(self, n: int) -> int:
        used = [False] * (n + 1)

        def place(position):
            if position > n:
                return 1
            total = 0
            for num in range(1, n + 1):
                if not used[num] and (num % position == 0 or position % num == 0):
                    used[num] = True
                    total += place(position + 1)
                    used[num] = False
            return total

        return place(1)
