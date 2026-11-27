# LeetCode 2146. K Highest Ranked Items Within a Price Range — Medium
# https://leetcode.com/problems/k-highest-ranked-items-within-a-price-range/
# Submission 2204474705 — Accepted, Python3
#
# My thinking: the rank is by distance from the start, then price, then
# row, then column — exactly the order a breadth-first search visits
# cells in when ties are broken that way. I BFS over the non-zero cells,
# collect every cell whose price is in range, sort by (distance, price,
# row, column), and return the first k positions.
class Solution:
    def highestRankedKItems(self, grid: list[list[int]], pricing: list[int], start: list[int], k: int) -> list[list[int]]:
        from collections import deque
        low, high = pricing
        m, n = len(grid), len(grid[0])
        sr, sc = start
        dist = [[-1] * n for _ in range(m)]
        dist[sr][sc] = 0
        q = deque([(sr, sc)])
        items = []
        while q:
            r, c = q.popleft()
            price = grid[r][c]
            if low <= price <= high:
                items.append((dist[r][c], price, r, c))
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] != 0 and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))
        items.sort()
        return [[r, c] for _, _, r, c in items[:k]]
