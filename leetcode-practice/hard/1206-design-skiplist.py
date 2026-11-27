import random


class Skiplist:
    # My thinking: a tower of linked lists — the top levels
    # skip ahead, the bottom level holds every value, and a
    # coin flip decides how tall each new tower grows.
    class Node:
        __slots__ = ("val", "next")

        def __init__(self, val, levels):
            self.val = val
            self.next = [None] * levels

    def __init__(self):
        self.max_levels = 16
        self.head = self.Node(-1, self.max_levels)
        self.levels = 1

    def _random_levels(self):
        levels = 1
        while levels < self.max_levels and random.random() < 0.5:
            levels += 1
        return levels

    def _find(self, target):
        update = [None] * self.max_levels
        node = self.head
        for level in range(self.levels - 1, -1, -1):
            while node.next[level] is not None and node.next[level].val < target:
                node = node.next[level]
            update[level] = node
        return update

    def search(self, target: int) -> bool:
        update = self._find(target)
        nxt = update[0].next[0]
        return nxt is not None and nxt.val == target

    def add(self, num: int) -> None:
        update = self._find(num)
        levels = self._random_levels()
        if levels > self.levels:
            for level in range(self.levels, levels):
                update[level] = self.head
            self.levels = levels
        node = self.Node(num, levels)
        for level in range(levels):
            node.next[level] = update[level].next[level]
            update[level].next[level] = node

    def erase(self, num: int) -> bool:
        update = self._find(num)
        nxt = update[0].next[0]
        if nxt is None or nxt.val != num:
            return False
        for level in range(self.levels):
            if update[level].next[level] is nxt:
                update[level].next[level] = nxt.next[level]
        while self.levels > 1 and self.head.next[self.levels - 1] is None:
            self.levels -= 1
        return True
