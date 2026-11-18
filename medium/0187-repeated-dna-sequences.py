# LeetCode 187. Repeated DNA Sequences — Medium
# https://leetcode.com/problems/repeated-dna-sequences/
# Submission 2198439896 — Accepted, Python3
#
# My thinking: I slide a window of 10 letters along
# the string and note every piece I see. The first
# time a piece shows up again it joins the answer,
# and a set keeps it from being reported twice no
# matter how often it repeats.

from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()
        repeated = set()
        for i in range(len(s) - 9):
            piece = s[i:i + 10]
            if piece in seen:
                repeated.add(piece)
            seen.add(piece)
        return list(repeated)
