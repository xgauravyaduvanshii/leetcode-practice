# LeetCode 2056. Number of Valid Move Combinations On Chessboard — Hard
# https://leetcode.com/problems/number-of-valid-move-combinations-on-chessboard/
# Submission 2201562898 — Accepted, Python3
#
# My thinking: I list every move each piece can
# make, then try the pieces one by one — a move
# only counts if no two pieces ever share a
# square at the same moment or swap places.

class Solution:
    def countCombinations(self, pieces: list[str], positions: list[list[int]]) -> int:
        dirs = {
            'rook': [(1, 0), (-1, 0), (0, 1), (0, -1)],
            'bishop': [(1, 1), (1, -1), (-1, 1), (-1, -1)],
            'queen': [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)],
        }
        moves = []
        for piece, (r, c) in zip(pieces, positions):
            opts = [[(r, c)]]
            for dr, dc in dirs[piece]:
                nr, nc = r, c
                path = [(r, c)]
                while True:
                    nr += dr
                    nc += dc
                    if not (1 <= nr <= 8 and 1 <= nc <= 8):
                        break
                    path.append((nr, nc))
                    opts.append(list(path))
            moves.append(opts)
        n = len(pieces)
        chosen = [None] * n
        count = [0]

        def at(path, t):
            return path[t] if t < len(path) else path[-1]

        def conflicts(p, q):
            m = max(len(p), len(q))
            for t in range(m):
                if at(p, t) == at(q, t):
                    return True
                if t + 1 < m and at(p, t) == at(q, t + 1) and at(p, t + 1) == at(q, t):
                    return True
            return False

        def dfs(i):
            if i == n:
                count[0] += 1
                return
            for opt in moves[i]:
                ok = True
                for j in range(i):
                    if conflicts(opt, chosen[j]):
                        ok = False
                        break
                if ok:
                    chosen[i] = opt
                    dfs(i + 1)
                    chosen[i] = None

        dfs(0)
        return count[0]
