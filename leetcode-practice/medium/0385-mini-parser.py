# LeetCode 385. Mini Parser — Medium
# https://leetcode.com/problems/mini-parser/
# Submission 2198767162 — Accepted, Python3
#
# My thinking: a plain number is the base case. For
# a list I scan the string once with a stack — an
# opening bracket pushes a new empty list, a closing
# bracket pops the finished list into its parent,
# and digits build up into numbers along the way.

class Solution:
    def deserialize(self, s: str):
        if s[0] != "[":
            return NestedInteger(int(s))
        stack = []
        number = ""
        for char in s:
            if char == "[":
                stack.append(NestedInteger())
            elif char == "]":
                if number:
                    stack[-1].add(NestedInteger(int(number)))
                    number = ""
                top = stack.pop()
                if stack:
                    stack[-1].add(top)
                else:
                    return top
            elif char == ",":
                if number:
                    stack[-1].add(NestedInteger(int(number)))
                    number = ""
            else:
                number += char
