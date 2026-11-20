import math


class Solution:
    def visiblePoints(self, points: list[list[int]], angle: int, location: list[int]) -> int:
        # My thinking: the points sitting on you are always
        # seen — for the rest, line up their angles and slide
        # a window as wide as your field of view.
        lx, ly = location
        same = 0
        angles = []
        for x, y in points:
            if x == lx and y == ly:
                same += 1
            else:
                angles.append(math.degrees(math.atan2(y - ly, x - lx)))
        angles.sort()
        n = len(angles)
        angles += [a + 360 for a in angles]
        best = 0
        j = 0
        for i in range(n):
            while angles[j] - angles[i] <= angle:
                j += 1
            best = max(best, j - i)
        return same + best
