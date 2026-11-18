# LeetCode 735. Asteroid Collision — Medium
# https://leetcode.com/problems/asteroid-collision/
# Submission 2198923814 — Accepted, Python3
#
# My thinking: only a right-moving rock meeting a
# left-moving one can collide. I keep the
# survivors on a stack — the smaller one bursts,
# equal ones both burst, and the bigger one keeps
# going.

from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for rock in asteroids:
            while stack and stack[-1] > 0 and rock < 0:
                if stack[-1] < -rock:
                    stack.pop()
                elif stack[-1] == -rock:
                    stack.pop()
                    break
                else:
                    break
            else:
                stack.append(rock)
        return stack
