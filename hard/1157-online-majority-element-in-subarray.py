import bisect


class MajorityChecker:
    # My thinking: a segment tree stores each range's Boyer-Moore
    # candidate, and the real count comes from the candidate's
    # occurrence list — a query is right when it clears the bar.
    def __init__(self, arr: list[int]):
        self.n = len(arr)
        self.positions = {}
        for i, num in enumerate(arr):
            self.positions.setdefault(num, []).append(i)
        size = 1
        while size < self.n:
            size *= 2
        self.size = size
        self.tree = [(0, 0)] * (2 * size)
        for i, num in enumerate(arr):
            self.tree[size + i] = (num, 1)
        for i in range(size - 1, 0, -1):
            self.tree[i] = self._merge(self.tree[2 * i], self.tree[2 * i + 1])

    @staticmethod
    def _merge(left, right):
        if left[0] == right[0]:
            return (left[0], left[1] + right[1])
        if left[1] > right[1]:
            return (left[0], left[1] - right[1])
        return (right[0], right[1] - left[1])

    def _query(self, left, right):
        left += self.size
        right += self.size
        left_res = (0, 0)
        right_res = (0, 0)
        while left <= right:
            if left % 2 == 1:
                left_res = self._merge(left_res, self.tree[left])
                left += 1
            if right % 2 == 0:
                right_res = self._merge(self.tree[right], right_res)
                right -= 1
            left //= 2
            right //= 2
        return self._merge(left_res, right_res)

    def query(self, left: int, right: int, threshold: int) -> int:
        candidate, _ = self._query(left, right)
        positions = self.positions.get(candidate, [])
        count = bisect.bisect_right(positions, right) - bisect.bisect_left(positions, left)
        return candidate if count >= threshold else -1
