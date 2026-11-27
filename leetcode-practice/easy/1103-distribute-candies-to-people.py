# LeetCode 1103. Distribute Candies to People — Easy
# https://leetcode.com/problems/distribute-candies-to-people/
# Submission 2197556737 — Accepted, Python3
#
# My thinking: I hand out 1, then 2, then 3 candies
# and so on, going round the people in turn. If
# fewer candies are left than the next amount, I
# just give what is left and stop.

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> list[int]:
        result = [0] * num_people
        give = 1
        i = 0
        while candies > 0:
            result[i] += min(give, candies)
            candies -= give
            give += 1
            i = (i + 1) % num_people
        return result
