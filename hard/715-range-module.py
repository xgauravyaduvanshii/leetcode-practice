import bisect


class RangeModule:
    def __init__(self):
        # My thinking: keep the tracked ranges sorted and disjoint;
        # adding merges everything it touches, removing cuts holes,
        # and a query is a check that one range covers the whole span.
        self.intervals = []  # list of [start, end), disjoint, sorted

    def addRange(self, left: int, right: int) -> None:
        intervals = self.intervals
        starts = [iv[0] for iv in intervals]
        i = bisect.bisect_left(starts, left)
        # Merge with the previous interval if it reaches left.
        if i > 0 and intervals[i - 1][1] >= left:
            i -= 1
        new_left, new_right = left, right
        j = i
        while j < len(intervals) and intervals[j][0] <= new_right:
            new_left = min(new_left, intervals[j][0])
            new_right = max(new_right, intervals[j][1])
            j += 1
        intervals[i:j] = [[new_left, new_right]]

    def queryRange(self, left: int, right: int) -> bool:
        intervals = self.intervals
        starts = [iv[0] for iv in intervals]
        i = bisect.bisect_right(starts, left) - 1
        return i >= 0 and intervals[i][1] >= right

    def removeRange(self, left: int, right: int) -> None:
        intervals = self.intervals
        starts = [iv[0] for iv in intervals]
        i = bisect.bisect_left(starts, left)
        if i > 0 and intervals[i - 1][1] > left:
            i -= 1
        new_pieces = []
        j = i
        while j < len(intervals) and intervals[j][0] < right:
            s, e = intervals[j]
            if s < left:
                new_pieces.append([s, left])
            if e > right:
                new_pieces.append([right, e])
            j += 1
        intervals[i:j] = new_pieces
