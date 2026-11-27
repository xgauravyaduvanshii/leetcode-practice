# LeetCode 478. Generate Random Point in a Circle — Medium
# https://leetcode.com/problems/generate-random-point-in-a-circle/
# Submission 2198821004 — Accepted, Python3
#
# My thinking: a random angle and a radius scaled
# by the square root of a uniform draw spread points
# evenly over the disc — the square root corrects
# for the area growing with the radius.

import math
import random


class Solution:
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self):
        length = math.sqrt(random.random()) * self.radius
        angle = random.random() * 2 * math.pi
        return [
            self.x_center + length * math.cos(angle),
            self.y_center + length * math.sin(angle),
        ]
