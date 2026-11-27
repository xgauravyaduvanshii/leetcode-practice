# LeetCode 2491. Divide Players Into Teams of Equal Skill — Medium
# https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/
# Submission 2197793596 — Accepted, Python3
#
# My thinking: after sorting, the weakest and
# strongest players must be on the same team, which
# fixes the target skill sum for every team. I pair
# smallest with largest and check every pair adds
# up to that target, adding up each pair's product.

class Solution:
    def dividePlayers(self, skill: list[int]) -> int:
        skill.sort()
        n = len(skill)
        target = skill[0] + skill[-1]
        total = 0
        for i in range(n // 2):
            if skill[i] + skill[n - 1 - i] != target:
                return -1
            total += skill[i] * skill[n - 1 - i]
        return total
