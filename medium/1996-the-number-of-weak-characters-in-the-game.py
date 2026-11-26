# LeetCode 1996. The Number of Weak Characters in the Game — Medium
# https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/
# Submission 2204115605 — Accepted, Python3
#
# My thinking: A character is weak only if some other character beats
# it on both attack and defense, so I sort by attack from highest to
# lowest. Characters with the same attack can never make each other
# weak, so inside one attack group I sort defense from lowest to
# highest. Then I walk the sorted list keeping the best defense I have
# seen so far, which always comes from a strictly higher attack. If the
# current character's defense is below that best defense, a stronger
# character exists on both counts and it is weak. Otherwise I update
# the best defense with this character's defense and move on.

from typing import List


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda p: (-p[0], p[1]))
        weak = 0
        max_defense = 0
        for _, defense in properties:
            if defense < max_defense:
                weak += 1
            else:
                max_defense = defense
        return weak
