class SummaryRanges:
    def __init__(self):
        # My thinking: keep the intervals sorted and disjoint; a new
        # number either joins a neighbouring interval or starts its
        # own, and neighbours merge when they touch.
        self.intervals = []

    def addNum(self, value: int) -> None:
        intervals = self.intervals
        # First interval whose start is greater than the new value.
        lo, hi = 0, len(intervals)
        while lo < hi:
            mid = (lo + hi) // 2
            if intervals[mid][0] > value:
                hi = mid
            else:
                lo = mid + 1
        pos = lo
        # Merge into the previous interval if it reaches the value.
        if pos > 0 and intervals[pos - 1][1] + 1 >= value:
            pos -= 1
            intervals[pos][1] = max(intervals[pos][1], value)
        else:
            intervals.insert(pos, [value, value])
        # Merge any following intervals that now touch this one.
        while pos + 1 < len(intervals) and intervals[pos][1] + 1 >= intervals[pos + 1][0]:
            intervals[pos][1] = max(intervals[pos][1], intervals[pos + 1][1])
            intervals.pop(pos + 1)

    def getIntervals(self) -> list[list[int]]:
        return self.intervals
