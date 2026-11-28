# LeetCode 2556. Disconnect Path in a Binary Matrix by at Most One Flip — Medium
# https://leetcode.com/problems/disconnect-path-in-a-binary-matrix-by-at-most-one-flip/
# Submission 2205066078 — Accepted, Python3
#
# My thinking: find one path with DFS. If none exists, the grid
# is already disconnected. Otherwise try to find a second path
# that avoids the first path's inner cells: if one exists, two
# disjoint paths survive any single flip; if not, some cell of
# the first path is a bottleneck and flipping it disconnects.
class Solution:
    def isPossibleToCutPath(self, grid: list[list[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        if grid[0][0] == 0 or grid[m - 1][n - 1] == 0:
            return True

        def find_path(blocked):
            start = (0, 0)
            parent = {start: None}
            stack = [start]
            while stack:
                r, c = stack.pop()
                if (r, c) == (m - 1, n - 1):
                    path = []
                    cur = (r, c)
                    while cur is not None:
                        path.append(cur)
                        cur = parent[cur]
                    return path[::-1]
                for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1
                            and (nr, nc) not in parent and (nr, nc) not in blocked):
                        parent[(nr, nc)] = (r, c)
                        stack.append((nr, nc))
            return None

        path = find_path(set())
        if path is None:
            return True
        return find_path(set(path[1:-1])) is None
