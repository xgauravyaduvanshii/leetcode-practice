class Solution:
    def gridIllumination(self, n: int, lamps: list[list[int]], queries: list[list[int]]) -> list[int]:
        # My thinking: a cell is lit when its row, column, or
        # either diagonal holds a lamp — keep counts per line, and
        # switch off the lamps around each queried cell.
        lamps_set = set()
        rows = {}
        cols = {}
        diag1 = {}
        diag2 = {}
        for r, c in lamps:
            if (r, c) in lamps_set:
                continue
            lamps_set.add((r, c))
            rows[r] = rows.get(r, 0) + 1
            cols[c] = cols.get(c, 0) + 1
            diag1[r - c] = diag1.get(r - c, 0) + 1
            diag2[r + c] = diag2.get(r + c, 0) + 1
        result = []
        for r, c in queries:
            if rows.get(r, 0) or cols.get(c, 0) or diag1.get(r - c, 0) or diag2.get(r + c, 0):
                result.append(1)
            else:
                result.append(0)
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    nr, nc = r + dr, c + dc
                    if (nr, nc) in lamps_set:
                        lamps_set.discard((nr, nc))
                        rows[nr] -= 1
                        cols[nc] -= 1
                        diag1[nr - nc] -= 1
                        diag2[nr + nc] -= 1
        return result
