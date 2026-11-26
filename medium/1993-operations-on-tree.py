# LeetCode 1993. Operations on Tree — Medium
# https://leetcode.com/problems/operations-on-tree/
# Submission 2204111385 — Accepted, Python3

# My thinking: keep each node's locker (None when unlocked) plus a
# children list built from the parent array. lock() needs the node
# free, no locked ancestor (walk up the parent chain) and no locked
# descendant (walk down the children). unlock() only succeeds for the
# user who locked the node. upgrade() needs the node free, at least
# one locked descendant and no locked ancestor, then it frees every
# locked descendant and locks the node itself.
class LockingTree:
    def __init__(self, parent):
        self.parent = parent
        self.locked = [None] * len(parent)
        self.children = [[] for _ in parent]
        for i, p in enumerate(parent):
            if p != -1:
                self.children[p].append(i)

    def _has_locked_ancestor(self, num):
        p = self.parent[num]
        while p != -1:
            if self.locked[p] is not None:
                return True
            p = self.parent[p]
        return False

    def _locked_descendants(self, num):
        found = []
        stack = list(self.children[num])
        while stack:
            node = stack.pop()
            if self.locked[node] is not None:
                found.append(node)
            stack.extend(self.children[node])
        return found

    def lock(self, num, user):
        if self.locked[num] is not None:
            return False
        if self._has_locked_ancestor(num):
            return False
        if self._locked_descendants(num):
            return False
        self.locked[num] = user
        return True

    def unlock(self, num, user):
        if self.locked[num] != user:
            return False
        self.locked[num] = None
        return True

    def upgrade(self, num, user):
        if self.locked[num] is not None:
            return False
        if self._has_locked_ancestor(num):
            return False
        desc = self._locked_descendants(num)
        if not desc:
            return False
        for node in desc:
            self.locked[node] = None
        self.locked[num] = user
        return True


if __name__ == "__main__":
    # Sample 1 from the problem statement.
    tree = LockingTree([-1, 0, 0, 1, 1, 2, 2])
    got = [
        tree.lock(2, 2),
        tree.unlock(2, 3),
        tree.unlock(2, 2),
        tree.lock(4, 5),
        tree.upgrade(0, 1),
        tree.lock(0, 1),
    ]
    assert got == [True, False, True, True, True, False], got

    # lock() fails when a descendant is already locked, and when an
    # ancestor is locked; upgrade() fails with no locked descendant.
    t2 = LockingTree([-1, 0, 0])
    assert t2.lock(1, 1) is True
    assert t2.lock(0, 1) is False
    assert t2.upgrade(2, 9) is False
    assert t2.upgrade(0, 1) is True
    assert t2.lock(1, 1) is False  # ancestor 0 is now locked
    assert t2.unlock(0, 2) is False  # wrong user
    assert t2.unlock(0, 1) is True
    print("All sample checks passed.")
