# LeetCode 2069. Walking Robot Simulation II — Medium
# https://leetcode.com/problems/walking-robot-simulation-ii/
# Submission 2204395350 — Accepted, Python3
#
# My thinking: walking around the perimeter repeats every
# 2*(width + height) - 4 steps, so I reduce any step count modulo
# that period first. Then I walk one cell at a time, turning right
# whenever the next cell would leave the grid, which traces the
# perimeter exactly. The direction cycles East, North, West, South.
class Robot:
    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height
        self.x = 0
        self.y = 0
        self.d = 0
        self.dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.per = 2 * (width + height) - 4

    def step(self, num: int) -> None:
        if num == 0 or self.per <= 0:
            return
        num %= self.per
        if num == 0:
            num = self.per
        for _ in range(num):
            for _ in range(4):
                dx, dy = self.dirs[self.d]
                nx, ny = self.x + dx, self.y + dy
                if 0 <= nx < self.w and 0 <= ny < self.h:
                    self.x, self.y = nx, ny
                    break
                self.d = (self.d + 1) % 4

    def getPos(self) -> list[int]:
        return [self.x, self.y]

    def getDir(self) -> str:
        return ["East", "North", "West", "South"][self.d]
