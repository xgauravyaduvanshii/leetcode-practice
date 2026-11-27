# LeetCode 331. Verify Preorder Serialization of a Binary Tree — Medium
# https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/
# Submission 2198748166 — Accepted, Python3
#
# My thinking: I count empty slots. The tree starts
# with one slot; every node takes a slot, and a
# non-null node opens two more. If the slots ever go
# negative the string is broken, and at the end
# exactly zero slots must remain.

class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        slots = 1
        for node in preorder.split(","):
            slots -= 1
            if slots < 0:
                return False
            if node != "#":
                slots += 2
        return slots == 0
