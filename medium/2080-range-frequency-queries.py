import bisect


class RangeFreqQuery:
    # My thinking: for each distinct value keep the sorted list of indices
    # where it appears. A query [left, right] for a value is then just two
    # binary searches on that value's list: how many indices fall inside
    # the range.
    def __init__(self, arr: list[int]):
        self.pos = {}
        for i, v in enumerate(arr):
            self.pos.setdefault(v, []).append(i)

    def query(self, left: int, right: int, value: int) -> int:
        lst = self.pos.get(value)
        if not lst:
            return 0
        lo = bisect.bisect_left(lst, left)
        hi = bisect.bisect_right(lst, right)
        return hi - lo
