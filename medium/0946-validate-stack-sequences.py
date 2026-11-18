# LeetCode 946. Validate Stack Sequences — Medium
# https://leetcode.com/problems/validate-stack-sequences/
# Submission 2198973487 — Accepted, Python3
#
# My thinking: I push the numbers in order and
# pop whenever the top of the stack matches the
# next number to come out. If the stack is empty
# at the end, the sequence was possible.

from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        pop_index = 0
        for value in pushed:
            stack.append(value)
            while stack and stack[-1] == popped[pop_index]:
                stack.pop()
                pop_index += 1
        return not stack
