# LeetCode 2383. Minimum Hours of Training to Win a Competition — Easy
# https://leetcode.com/problems/minimum-hours-of-training-to-win-a-competition/
# Submission 2197776423 — Accepted, Python3
#
# My thinking: before each opponent I train just
# enough so my energy and experience are both
# strictly greater than theirs. Training hours add
# up, and after each win I lose the opponent's
# energy but gain their experience.

class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: list[int], experience: list[int]) -> int:
        hours = 0
        e = initialEnergy
        x = initialExperience
        for en, ex in zip(energy, experience):
            if e <= en:
                need = en - e + 1
                hours += need
                e += need
            if x <= ex:
                need = ex - x + 1
                hours += need
                x += need
            e -= en
            x += ex
        return hours
