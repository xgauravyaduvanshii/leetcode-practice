# LeetCode 1282. Group the People Given the Group Size They Belong To — Medium
# https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/
# Submission 2199022935 — Accepted, Python3
#
# My thinking: I collect people into buckets by
# the size of group they want. The moment a
# bucket fills up, it becomes a finished group
# and the bucket starts over.

from collections import defaultdict
from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        buckets = defaultdict(list)
        result = []
        for person, size in enumerate(groupSizes):
            buckets[size].append(person)
            if len(buckets[size]) == size:
                result.append(buckets[size])
                buckets[size] = []
        return result
