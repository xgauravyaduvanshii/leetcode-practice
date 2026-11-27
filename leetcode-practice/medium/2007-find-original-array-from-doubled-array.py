# LeetCode 2007. Find Original Array From Doubled Array — Medium
# https://leetcode.com/problems/find-original-array-from-doubled-array/
# Submission 2204129510 — Accepted, Python3
#
# My thinking:
# The changed array is the original array plus a doubled copy of every
# element, so its length must be even — an odd length can never be a
# valid doubled array, so return [] right away.
# Sort the array first. Then the smallest unpaired number must be an
# original element, because its double is larger and cannot pair with
# anything smaller.
# Count how many times each value appears. Walk through the sorted
# values: for each value x that still has unpaired copies, we need the
# same number of copies of 2*x to pair with them. If there are not
# enough, no original array exists, so return [].
# Zero is special because 2*0 is 0, so zeros pair with each other — the
# count of zeros must be even, and half of them go into the answer.
# Each time we pair x with 2*x, we add one copy of x to the answer for
# every unpaired copy, and use up the matching copies of 2*x.

from collections import Counter
from typing import List


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 == 1:
            return []

        count = Counter(changed)
        original = []

        for x in sorted(count):
            if count[x] == 0:
                continue
            if x == 0:
                if count[0] % 2 == 1:
                    return []
                original.extend([0] * (count[0] // 2))
                count[0] = 0
                continue
            if count[2 * x] < count[x]:
                return []
            original.extend([x] * count[x])
            count[2 * x] -= count[x]
            count[x] = 0

        return original


if __name__ == "__main__":
    sol = Solution()
    assert sol.findOriginalArray([1, 3, 4, 2, 6, 8]) == [1, 3, 4]
    assert sol.findOriginalArray([6, 3, 0, 1]) == []
    assert sol.findOriginalArray([1]) == []
    assert sol.findOriginalArray([0, 0, 0, 0]) == [0, 0]
    assert sol.findOriginalArray([2, 4, 4, 8]) == [2, 4]
    assert sol.findOriginalArray([0, 0, 1]) == []
    print("All samples passed")
