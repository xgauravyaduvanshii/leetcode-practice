# LeetCode 3273. Minimum Amount of Damage Dealt to Bob — Hard
# https://leetcode.com/problems/minimum-amount-of-damage-dealt-to-bob/
# Submission 2202172302 — Accepted, Python3
#
# My thinking: an enemy with health h takes
# ceil(h / power) seconds to kill, dealing its
# damage every second until it dies. Killing
# the enemy with the smaller time-per-damage
# first is always better, so I sort by t / d
# and accumulate: each enemy adds its damage
# times the total time elapsed so far.

from typing import List


class Solution:
    def minDamage(self, power: int, damage: List[int], health: List[int]) -> int:
        enemies = []
        for d, h in zip(damage, health):
            t = (h + power - 1) // power
            enemies.append((t, d))
        enemies.sort(key=lambda x: x[0] / x[1])
        cur = 0
        ans = 0
        for t, d in enemies:
            cur += t
            ans += d * cur
        return ans
