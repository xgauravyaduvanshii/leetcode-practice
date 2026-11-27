class Solution:
    def pathsWithMaxScore(self, board: list[str]) -> list[int]:
        # My thinking: walk backwards from S to E, keeping the
        # best score and how many ways reach it — and track
        # reachability by score, since a count of 0 modulo
        # 1e9+7 does not mean the cell is unreachable.
        MOD = 10 ** 9 + 7
        n = len(board)
        NEG = -10 ** 9
        score = [[NEG] * n for _ in range(n)]
        count = [[0] * n for _ in range(n)]
        score[n - 1][n - 1] = 0
        count[n - 1][n - 1] = 1
        for r in range(n - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if board[r][c] == "X":
                    continue
                if r == n - 1 and c == n - 1:
                    continue
                best = NEG
                ways = 0
                for nr, nc in ((r + 1, c), (r, c + 1), (r + 1, c + 1)):
                    if nr < n and nc < n and score[nr][nc] != NEG:
                        if score[nr][nc] > best:
                            best = score[nr][nc]
                            ways = count[nr][nc]
                        elif score[nr][nc] == best:
                            ways = (ways + count[nr][nc]) % MOD
                if best == NEG:
                    continue
                add = 0 if board[r][c] in "ES" else int(board[r][c])
                score[r][c] = best + add
                count[r][c] = ways
        if score[0][0] == NEG:
            return [0, 0]
        return [score[0][0], count[0][0]]
