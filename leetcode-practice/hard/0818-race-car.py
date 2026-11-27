# LeetCode 818. Race Car — Hard
# https://leetcode.com/problems/race-car/
# Submission 2198679039 — Accepted, Python3
#
# My thinking: the car has only two moves — speed up
# or turn around — so I search breadth-first over
# (position, speed) states. Positions stay between
# zero and twice the target, which keeps the search
# small, and the first time I land on the target the
# step count is the smallest possible.

from collections import deque


class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(0, 1, 0)])
        seen = {(0, 1)}
        while queue:
            pos, speed, steps = queue.popleft()
            if pos == target:
                return steps
            new_pos, new_speed = pos + speed, speed * 2
            if (new_pos, new_speed) not in seen and 0 < new_pos < 2 * target:
                seen.add((new_pos, new_speed))
                queue.append((new_pos, new_speed, steps + 1))
            new_speed = -1 if speed > 0 else 1
            if (pos, new_speed) not in seen:
                seen.add((pos, new_speed))
                queue.append((pos, new_speed, steps + 1))
        return -1
