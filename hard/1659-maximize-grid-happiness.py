from functools import lru_cache


class Solution:
    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
        # My thinking: fill the grid one cell at a time — an
        # introvert starts at 120 and loses 30 per neighbour,
        # an extrovert starts at 40 and gains 20 per neighbour,
        # so a new cell only changes itself and the neighbours
        # above and to its left.
        @lru_cache(maxsize=None)
        def dp(idx, intro, extro, above, cur):
            if idx == m * n:
                return 0
            i, j = divmod(idx, n)
            if j == n - 1:
                best = dp(idx + 1, intro, extro, cur, (0,) * n)  # leave empty, row ends
            else:
                best = dp(idx + 1, intro, extro, above, cur)  # leave empty
            neigh = []
            if i > 0:
                neigh.append(above[j])
            if j > 0:
                neigh.append(cur[j - 1])
            for kind, left, base, own in ((1, intro, 120, -30), (2, extro, 40, 20)):
                if left == 0:
                    continue
                gain = base
                for nb in neigh:
                    if nb == 0:
                        continue
                    gain += own  # this person vs the neighbour
                    gain += -30 if nb == 1 else 20  # neighbour vs this person
                new_cur = cur[:j] + (kind,) + cur[j + 1:]
                new_above = above
                if j == n - 1:
                    new_above = new_cur
                    new_cur = (0,) * n
                val = gain + dp(idx + 1, intro - (kind == 1), extro - (kind == 2), new_above, new_cur)
                best = max(best, val)
            return best

        return dp(0, introvertsCount, extrovertsCount, (0,) * n, (0,) * n)
