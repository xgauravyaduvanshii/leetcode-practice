class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        # My thinking: always fill the lowest, leftmost empty
        # cell, trying every square that fits there — with the
        # best count seen so far and a memory of the cheapest
        # way each skyline was reached.
        if n > m:
            n, m = m, n
        heights = [0] * m
        best = [max(n, m)]
        seen = {}

        def dfs(count):
            if count >= best[0]:
                return
            state = tuple(heights)
            if seen.get(state, float("inf")) <= count:
                return
            seen[state] = count
            if min(heights) == n:
                best[0] = count
                return
            min_h = min(heights)
            i = heights.index(min_h)
            max_size = 1
            while i + max_size < m and heights[i + max_size] == min_h and min_h + max_size < n:
                max_size += 1
            for size in range(max_size, 0, -1):
                for j in range(i, i + size):
                    heights[j] += size
                dfs(count + 1)
                for j in range(i, i + size):
                    heights[j] -= size

        dfs(0)
        return best[0]
