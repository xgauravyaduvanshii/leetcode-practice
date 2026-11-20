class Solution:
    def numSubmatrixSumTarget(self, matrix: list[list[int]], target: int) -> int:
        # My thinking: squash each pair of top and bottom rows
        # into one column-sum array, then count the subarrays
        # hitting the target with a running-sum map.
        rows = len(matrix)
        cols = len(matrix[0])
        total = 0
        for top in range(rows):
            col_sums = [0] * cols
            for bottom in range(top, rows):
                for c in range(cols):
                    col_sums[c] += matrix[bottom][c]
                seen = {0: 1}
                running = 0
                for value in col_sums:
                    running += value
                    total += seen.get(running - target, 0)
                    seen[running] = seen.get(running, 0) + 1
        return total
