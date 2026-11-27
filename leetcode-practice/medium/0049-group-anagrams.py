from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # My thinking: anagrams share the same sorted letters, so sort each
        # word and use the sorted form as a key — all words with the same
        # key belong in one group.
        groups = defaultdict(list)
        for s in strs:
            groups["".join(sorted(s))].append(s)
        return list(groups.values())
