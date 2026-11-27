# LeetCode 341. Flatten Nested List Iterator — Medium
# https://leetcode.com/problems/flatten-nested-list-iterator/
# Submission 2198754768 — Accepted, Python3
#
# My thinking: I flatten the whole nested list once
# in the constructor, walking it depth-first and
# keeping the plain integers in order. Next and
# hasNext then just walk that flat list with an
# index.

class NestedIterator:
    def __init__(self, nestedList):
        self._flat = []
        self._index = 0
        self._flatten(nestedList)

    def _flatten(self, nested_list):
        for item in nested_list:
            if item.isInteger():
                self._flat.append(item.getInteger())
            else:
                self._flatten(item.getList())

    def next(self):
        value = self._flat[self._index]
        self._index += 1
        return value

    def hasNext(self):
        return self._index < len(self._flat)
