# LeetCode 382. Linked List Random Node — Medium
# https://leetcode.com/problems/linked-list-random-node/
# Submission 2198766105 — Accepted, Python3
#
# My thinking: I do not know the length up front, so
# I walk the list once and keep each node with
# probability one over how many I have seen so far.
# That reservoir trick leaves every node equally
# likely to be the one I end up with.

import random


class Solution:
    def __init__(self, head):
        self.head = head

    def getRandom(self) -> int:
        chosen = None
        node = self.head
        count = 0
        while node:
            count += 1
            if random.randint(1, count) == 1:
                chosen = node.val
            node = node.next
        return chosen
