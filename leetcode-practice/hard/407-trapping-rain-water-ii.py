import heapq


class Solution:
    def trapRainWater(self, heightMap: list[list[int]]) -> int:
        # My thinking: water escapes over the lowest border, so flood
        # inwards from the border, always through the lowest wall
        # seen so far — anything lower than that wall holds water up
        # to the wall's height.
        if not heightMap or not heightMap[0]:
            return 0
        rows, cols = len(heightMap), len(heightMap[0])
        if rows < 3 or cols < 3:
            return 0
        visited = [[False] * cols for _ in range(rows)]
        heap = []
        for r in range(rows):
            for c in (0, cols - 1):
                heapq.heappush(heap, (heightMap[r][c], r, c))
                visited[r][c] = True
        for c in range(1, cols - 1):
            for r in (0, rows - 1):
                heapq.heappush(heap, (heightMap[r][c], r, c))
                visited[r][c] = True
        water = 0
        while heap:
            height, r, c = heapq.heappop(heap)
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                    visited[nr][nc] = True
                    water += max(0, height - heightMap[nr][nc])
                    heapq.heappush(heap, (max(height, heightMap[nr][nc]), nr, nc))
        return water
