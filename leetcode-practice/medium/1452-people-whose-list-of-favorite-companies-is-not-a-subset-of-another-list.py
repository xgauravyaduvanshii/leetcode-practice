# LeetCode 1452. People Whose List of Favorite Companies Is Not a Subset of Another List — Medium
# https://leetcode.com/problems/people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list/
# Submission 2199853812 — Accepted, Python3
#
# My thinking: I turn each person's list into
# a set. A person stays in the answer when no
# other person's set fully covers theirs.

from typing import List


class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        sets = [set(companies) for companies in favoriteCompanies]
        result = []
        for i, companies in enumerate(sets):
            if not any(i != j and companies <= other for j, other in enumerate(sets)):
                result.append(i)
        return result
