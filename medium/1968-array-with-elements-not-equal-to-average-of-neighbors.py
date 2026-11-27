# LeetCode 1968. Array With Elements Not Equal to Average of Neighbors — Medium
# https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/
# Submission 2204262930 — Accepted, Python3
#
# My thinking: an element is safe when it is not the average of its
# two neighbours, which is guaranteed if it sits strictly above both
# of them or strictly below both of them. So I sort the numbers,
# split them into a smaller half and a larger half, and weave the
# halves together large-small-large-small: every small element then
# sits between two larger ones, and every large element between two
# smaller ones, so no element can be the average of its neighbours.
# When the array is odd the smaller half has one extra element, and
# it goes at the end, where it has only one neighbour and needs no
# check at all.
class Solution:
    def rearrangeArray(self, nums):
        nums.sort()
        n = len(nums)
        mid = (n + 1) // 2
        small, large = nums[:mid], nums[mid:]
        out = []
        for i in range(len(large)):
            out.append(large[i])
            out.append(small[i])
        if len(small) > len(large):
            out.append(small[-1])
        return out
