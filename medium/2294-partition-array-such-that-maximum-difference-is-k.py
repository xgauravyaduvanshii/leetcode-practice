# LeetCode 2294. Partition Array Such That Maximum Difference Is K — Medium
# https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/
# Submission 2204654828 — Accepted, Python3
#
# My thinking: sort the array. A greedy pass works: start a group at the
# smallest unused number and keep adding numbers while they are within k
# of the group's first number. The moment a number is too far away, it
# must start a new group — any valid grouping has to cut there too, so
# the greedy count is minimal.
class Solution:
    def partitionArray(self, nums: list[int], k: int) -> int:
        nums.sort()
        ans = 1
        start = nums[0]
        for x in nums[1:]:
            if x - start > k:
                ans += 1
                start = x
        return ans
