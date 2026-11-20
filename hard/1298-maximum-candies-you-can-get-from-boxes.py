from collections import deque


class Solution:
    def maxCandies(self, status: list[int], candies: list[int], keys: list[list[int]], containedBoxes: list[list[int]], initialBoxes: list[int]) -> int:
        # My thinking: keep every box we hold; open the ones we
        # have keys for, and whenever a new key or a new box
        # arrives, retry the boxes still waiting.
        n = len(status)
        have = [False] * n
        opened = [False] * n
        has_key = [s == 1 for s in status]
        queue = deque(initialBoxes)
        for box in initialBoxes:
            have[box] = True
        total = 0
        while queue:
            box = queue.popleft()
            if opened[box] or not has_key[box]:
                continue
            opened[box] = True
            total += candies[box]
            for key in keys[box]:
                if not has_key[key]:
                    has_key[key] = True
                    if have[key] and not opened[key]:
                        queue.append(key)
            for inner in containedBoxes[box]:
                if not have[inner]:
                    have[inner] = True
                    if has_key[inner]:
                        queue.append(inner)
        return total
