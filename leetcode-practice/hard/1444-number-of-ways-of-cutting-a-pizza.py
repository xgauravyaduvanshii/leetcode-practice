from functools import lru_cache


class Solution:
    def ways(self, pizza: list[str], k: int) -> int:
        # My thinking: from each corner, every cut either
        # peels off a strip with an apple in it or keeps the
        # rest for the remaining cuts — a table of apple
        # counts tells which cuts are legal.
        MOD = 10 ** 9 + 7
        rows, cols = len(pizza), len(pizza[0])
        apples = [[0] * (cols + 1) for _ in range(rows + 1)]
        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                apples[r][c] = (1 if pizza[r][c] == "A" else 0) + apples[r + 1][c] + apples[r][c + 1] - apples[r + 1][c + 1]

        @lru_cache(maxsize=None)
        def dp(pieces, r, c):
            if apples[r][c] == 0:
                return 0
            if pieces == 1:
                return 1
            total = 0
            for nr in range(r + 1, rows):
                if apples[r][c] - apples[nr][c] > 0:
                    total = (total + dp(pieces - 1, nr, c)) % MOD
            for nc in range(c + 1, cols):
                if apples[r][c] - apples[r][nc] > 0:
                    total = (total + dp(pieces - 1, r, nc)) % MOD
            return total

        return dp(k, 0, 0)
