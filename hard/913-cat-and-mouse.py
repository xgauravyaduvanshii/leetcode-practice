from collections import deque


class Solution:
    def catMouseGame(self, graph: list[list[int]]) -> int:
        # My thinking: the game is a graph of (mouse, cat, turn)
        # states — work backwards from the wins, and a state that
        # can never be forced is a draw.
        n = len(graph)
        # outcome: 0 = draw, 1 = mouse wins, 2 = cat wins
        outcome = [[[0, 0] for _ in range(n)] for _ in range(n)]
        degree = [[[0, 0] for _ in range(n)] for _ in range(n)]
        queue = deque()
        for m in range(n):
            for c in range(n):
                degree[m][c][0] = len(graph[m])
                degree[m][c][1] = len(graph[c]) - (1 if 0 in graph[c] else 0)
        for i in range(n):
            for turn in range(2):
                outcome[0][i][turn] = 1
                queue.append((0, i, turn))
                if i != 0:
                    outcome[i][i][turn] = 2
                    queue.append((i, i, turn))
        while queue:
            m, c, turn = queue.popleft()
            result = outcome[m][c][turn]
            if turn == 0:
                # The previous move was the cat's.
                for prev_c in graph[c]:
                    if prev_c == 0:
                        continue
                    if outcome[m][prev_c][1] != 0:
                        continue
                    if result == 2:
                        outcome[m][prev_c][1] = 2
                        queue.append((m, prev_c, 1))
                    else:
                        degree[m][prev_c][1] -= 1
                        if degree[m][prev_c][1] == 0:
                            outcome[m][prev_c][1] = 1
                            queue.append((m, prev_c, 1))
            else:
                # The previous move was the mouse's.
                for prev_m in graph[m]:
                    if outcome[prev_m][c][0] != 0:
                        continue
                    if result == 1:
                        outcome[prev_m][c][0] = 1
                        queue.append((prev_m, c, 0))
                    else:
                        degree[prev_m][c][0] -= 1
                        if degree[prev_m][c][0] == 0:
                            outcome[prev_m][c][0] = 2
                            queue.append((prev_m, c, 0))
        return outcome[1][2][0]
