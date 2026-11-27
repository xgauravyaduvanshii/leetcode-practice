import math


class Solution:
    def numPoints(self, darts: list[list[int]], r: int) -> int:
        # My thinking: the best circle can always be slid
        # until two darts sit on its edge — so try every
        # circle through each pair of darts, and every circle
        # centred on a dart, and count what each one holds.
        n = len(darts)
        if n == 1:
            return 1
        best = 1
        for i in range(n):
            xi, yi = darts[i]
            count = 0
            for x, y in darts:
                if (x - xi) ** 2 + (y - yi) ** 2 <= r * r + 1e-9:
                    count += 1
            best = max(best, count)
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = darts[i]
                x2, y2 = darts[j]
                dx, dy = x2 - x1, y2 - y1
                d = math.hypot(dx, dy)
                if d > 2 * r + 1e-9 or d == 0:
                    continue
                mx, my = (x1 + x2) / 2, (y1 + y2) / 2
                h = math.sqrt(max(0.0, r * r - (d / 2) ** 2))
                ux, uy = -dy / d, dx / d
                for sign in (1, -1):
                    cx, cy = mx + sign * h * ux, my + sign * h * uy
                    count = 0
                    for x, y in darts:
                        if (x - cx) ** 2 + (y - cy) ** 2 <= r * r + 1e-9:
                            count += 1
                    best = max(best, count)
        return best
