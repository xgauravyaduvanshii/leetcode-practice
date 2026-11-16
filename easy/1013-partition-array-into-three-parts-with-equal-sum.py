# LeetCode 1013. Partition Array Into Three Parts With Equal Sum — Easy
# https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/
# Submission 2197550831 — Accepted, Python3
#
# My thinking: the whole array has to split into
# three equal parts, so the total must divide by
# 3. I walk along adding numbers up — every time
# my running sum hits one third of the total, that
# is one part done. If I can find three such parts,
# the split works.

class Solution:
    def canThreePartsEqualSum(self, arr: list[int]) -> bool:
        total = sum(arr)
        if total % 3 != 0:
            return False
        part = total // 3
        count = 0
        running = 0
        for num in arr:
            running += num
            if running == part:
                count += 1
                running = 0
        return count >= 3
