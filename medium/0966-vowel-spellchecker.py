# LeetCode 966. Vowel Spellchecker — Medium
# https://leetcode.com/problems/vowel-spellchecker/
# Submission 2198977473 — Accepted, Python3
#
# My thinking: I check each query three ways —
# exact match first, then ignoring case, then
# ignoring which vowel it is. The first word in
# the list wins at each step, so I only record
# the first one I see.

from typing import List


class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        exact = set(wordlist)
        lower_map = {}
        vowel_map = {}
        for word in wordlist:
            lowered = word.lower()
            if lowered not in lower_map:
                lower_map[lowered] = word
            masked = "".join("*" if ch in "aeiou" else ch for ch in lowered)
            if masked not in vowel_map:
                vowel_map[masked] = word
        result = []
        for query in queries:
            if query in exact:
                result.append(query)
            elif query.lower() in lower_map:
                result.append(lower_map[query.lower()])
            else:
                masked = "".join("*" if ch in "aeiou" else ch for ch in query.lower())
                result.append(vowel_map.get(masked, ""))
        return result
