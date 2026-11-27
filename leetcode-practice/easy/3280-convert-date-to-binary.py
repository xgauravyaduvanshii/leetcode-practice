# 3280. Convert Date to Binary (Easy)
# https://leetcode.com/problems/convert-date-to-binary/
# Submission 2199994430 — Accepted, Python3
class Solution:
    def convertDateToBinary(self, date: str) -> str:
        # My thinking: split the date on the dashes and
        # write each part — year, month, day — in binary,
        # then join them back with dashes.
        return "-".join(bin(int(part))[2:] for part in date.split("-"))
