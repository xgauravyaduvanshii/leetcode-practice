# 3692. Majority Frequency Characters (Easy)
# https://leetcode.com/problems/majority-frequency-characters/
# Submission 2200044267 — Accepted, Python3
from collections import Counter, defaultdict


class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        # My thinking: group the letters by how often
        # they appear. The winning group is the one
        # with the most different letters — and if two
        # groups tie, the one whose letters appear more
        # often wins. Every letter in that group is
        # part of the answer.
        counts = Counter(s)
        groups = defaultdict(list)
        for ch, c in counts.items():
            groups[c].append(ch)
        best_freq = max(groups, key=lambda k: (len(groups[k]), k))
        return "".join(groups[best_freq])
