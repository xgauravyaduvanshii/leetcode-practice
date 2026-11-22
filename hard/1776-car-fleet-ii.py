# LeetCode 1776. Car Fleet II — Hard
# https://leetcode.com/problems/car-fleet-ii/
# Submission 2201158151 — Accepted, Python3
#
# My thinking: I walk from the back, keeping the
# cars ahead that are still worth catching — a car
# I am slower than can never be caught, and a car
# that crashes into the fleet ahead of it before I
# would reach it is no longer the one I chase.

class Solution:
    def getCollisionTimes(self, cars: list[list[int]]) -> list[float]:
        n = len(cars)
        ans = [-1.0] * n
        stack = []
        for i in range(n - 1, -1, -1):
            pos, speed = cars[i]
            while stack:
                j = stack[-1]
                pos_j, speed_j = cars[j]
                if speed <= speed_j:
                    stack.pop()
                    continue
                t = (pos_j - pos) / (speed - speed_j)
                if ans[j] == -1 or t <= ans[j]:
                    ans[i] = t
                    break
                stack.pop()
            stack.append(i)
        return ans
