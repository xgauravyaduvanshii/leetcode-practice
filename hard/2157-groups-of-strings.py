# LeetCode 2157. Groups of Strings — Hard
# https://leetcode.com/problems/groups-of-strings/
# Submission 2201593977 — Accepted, Python3
#
# My thinking: a word is just the set of its
# letters, so two words belong together when
# their sets are the same, differ by one
# letter, or swap one letter for another — I
# flip each letter in turn, and swap each
# letter for every letter it lacks, join
# whatever I find, and count the groups.

class Solution:
    def groupStrings(self, words: list[str]) -> list[int]:
        masks = []
        for w in words:
            m = 0
            for ch in w:
                m |= 1 << (ord(ch) - ord('a'))
            masks.append(m)
        index = {}
        parent = list(range(len(words)))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[ra] = rb

        for i, m in enumerate(masks):
            # Same set of letters: the words are identical.
            if m in index:
                union(i, index[m])
            else:
                index[m] = i
            for b in range(26):
                # Add or delete one letter.
                other = m ^ (1 << b)
                if other in index:
                    union(i, index[other])
                # Replace one letter with a letter it lacks.
                if m >> b & 1:
                    for c in range(26):
                        if not (m >> c & 1):
                            other = m ^ (1 << b) ^ (1 << c)
                            if other in index:
                                union(i, index[other])
        groups = {}
        for i in range(len(words)):
            r = find(i)
            groups[r] = groups.get(r, 0) + 1
        return [len(groups), max(groups.values())]
