import bisect


class Solution:
    def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        # My thinking: fix the left and right edges, squash each row
        # into one number, then the best rectangle for those edges is
        # the best sub-array sum no bigger than k — found with a
        # sorted list of prefix sums.
        rows, cols = len(matrix), len(matrix[0])
        best = float("-inf")
        for left in range(cols):
            row_sums = [0] * rows
            for right in range(left, cols):
                for r in range(rows):
                    row_sums[r] += matrix[r][right]
                prefix = [0]
                running = 0
                for s in row_sums:
                    running += s
                    # Need an earlier prefix >= running - k.
                    i = bisect.bisect_left(prefix, running - k)
                    if i < len(prefix):
                        best = max(best, running - prefix[i])
                    bisect.insort(prefix, running)
        return best
