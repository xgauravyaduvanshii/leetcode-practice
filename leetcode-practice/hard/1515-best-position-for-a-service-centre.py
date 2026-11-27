import math


class Solution:
    def getMinDistSum(self, positions: list[list[int]]) -> float:
        # My thinking: the best spot pulls toward every point
        # at once — so start at the middle and keep sliding
        # toward the weighted centre until it stops moving.
        x = sum(p[0] for p in positions) / len(positions)
        y = sum(p[1] for p in positions) / len(positions)
        for _ in range(100):
            num_x = num_y = den = 0.0
            for px, py in positions:
                d = math.hypot(px - x, py - y)
                if d < 1e-9:
                    continue
                num_x += px / d
                num_y += py / d
                den += 1 / d
            if den == 0:
                break
            new_x, new_y = num_x / den, num_y / den
            if math.hypot(new_x - x, new_y - y) < 1e-7:
                x, y = new_x, new_y
                break
            x, y = new_x, new_y
        return sum(math.hypot(px - x, py - y) for px, py in positions)
