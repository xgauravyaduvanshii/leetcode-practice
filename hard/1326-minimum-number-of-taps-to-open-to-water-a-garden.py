class Solution:
    def minTaps(self, n: int, ranges: list[int]) -> int:
        # My thinking: each tap waters one stretch of the garden,
        # so turn them into intervals and take the fewest that
        # cover the whole garden, always reaching as far as
        # possible from where we already stand.
        furthest = [0] * (n + 1)
        for i, r in enumerate(ranges):
            left = max(0, i - r)
            right = min(n, i + r)
            furthest[left] = max(furthest[left], right)
        taps = 0
        current_end = 0
        next_end = 0
        for i in range(n):
            next_end = max(next_end, furthest[i])
            if i == current_end:
                if next_end == current_end:
                    return -1
                taps += 1
                current_end = next_end
                if current_end >= n:
                    return taps
        return -1
