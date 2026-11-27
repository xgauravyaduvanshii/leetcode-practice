# LeetCode 1600. Throne Inheritance — Medium
# https://leetcode.com/problems/throne-inheritance/
# Submission 2199890722 — Accepted, Python3
#
# My thinking: the order is a pre-order walk
# of the family tree — a person, then their
# children in birth order. Death only hides a
# name; their children still inherit.

from collections import defaultdict
from typing import List


class ThroneInheritance:
    def __init__(self, kingName: str):
        self.king = kingName
        self.children = defaultdict(list)
        self.dead = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.children[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        order = []

        def dfs(name):
            if name not in self.dead:
                order.append(name)
            for child in self.children[name]:
                dfs(child)

        dfs(self.king)
        return order
