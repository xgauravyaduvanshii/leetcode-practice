# LeetCode 765. Couples Holding Hands — Hard
# https://leetcode.com/problems/couples-holding-hands/
# Submission 2198674402 — Accepted, Python3
#
# My thinking: I walk the row two seats at a time. If
# the person in the second seat is not the partner of
# the first, I swap in the partner from wherever they
# are sitting — one swap fixes that couple for good,
# so the total is the smallest possible.

from typing import List


class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        pos = {person: i for i, person in enumerate(row)}
        swaps = 0
        for seat in range(0, len(row), 2):
            partner = row[seat] ^ 1
            if row[seat + 1] != partner:
                partner_seat = pos[partner]
                row[seat + 1], row[partner_seat] = row[partner_seat], row[seat + 1]
                pos[row[seat + 1]] = seat + 1
                pos[row[partner_seat]] = partner_seat
                swaps += 1
        return swaps
