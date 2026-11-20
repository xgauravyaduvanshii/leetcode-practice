import heapq


class Solution:
    def kthSmallest(self, mat: list[list[int]], k: int) -> int:
        # My thinking: the smallest sum takes the first column
        # everywhere — then keep a heap of the next best sums,
        # each one bumping a single row to its next column.
        rows, cols = len(mat), len(mat[0])
        start = tuple([0] * rows)
        total = sum(mat[r][0] for r in range(rows))
        heap = [(total, start)]
        seen = {start}
        for _ in range(k - 1):
            total, idx = heapq.heappop(heap)
            for r in range(rows):
                if idx[r] + 1 < cols:
                    new_idx = list(idx)
                    new_idx[r] += 1
                    new_idx = tuple(new_idx)
                    if new_idx not in seen:
                        seen.add(new_idx)
                        heapq.heappush(heap, (total - mat[r][idx[r]] + mat[r][idx[r] + 1], new_idx))
        return heap[0][0]
