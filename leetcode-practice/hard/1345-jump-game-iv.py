from collections import deque


class Solution:
    def minJumps(self, arr: list[int]) -> int:
        # My thinking: breadth-first search from the start — the
        # neighbours are the two next to you plus every index
        # holding the same value, and each value's list is used
        # once so the walk never repeats itself.
        n = len(arr)
        if n == 1:
            return 0
        same = {}
        for i, val in enumerate(arr):
            same.setdefault(val, []).append(i)
        queue = deque([(0, 0)])
        seen = {0}
        while queue:
            i, steps = queue.popleft()
            for nxt in (i - 1, i + 1):
                if 0 <= nxt < n and nxt not in seen:
                    if nxt == n - 1:
                        return steps + 1
                    seen.add(nxt)
                    queue.append((nxt, steps + 1))
            for nxt in same.get(arr[i], []):
                if nxt not in seen:
                    if nxt == n - 1:
                        return steps + 1
                    seen.add(nxt)
                    queue.append((nxt, steps + 1))
            same[arr[i]] = []
        return -1
