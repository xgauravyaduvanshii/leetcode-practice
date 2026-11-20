from collections import deque


class Solution:
    def findMaxValueOfEquation(self, points: list[list[int]], k: int) -> int:
        # My thinking: with x already sorted, the value splits
        # into (y - x) from the left point plus (y + x) from
        # the right — so keep a sliding window of the best
        # left halves within reach.
        best = float("-inf")
        window = deque()
        for x, y in points:
            while window and x - window[0][0] > k:
                window.popleft()
            if window:
                best = max(best, window[0][1] + y + x)
            value = y - x
            while window and window[-1][1] <= value:
                window.pop()
            window.append((x, value))
        return best
