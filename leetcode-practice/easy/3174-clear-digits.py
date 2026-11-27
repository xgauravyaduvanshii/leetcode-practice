# 3174. Clear Digits (Easy)
# https://leetcode.com/problems/clear-digits/
# Submission 2199983566 — Accepted, Python3
class Solution:
    def clearDigits(self, s: str) -> str:
        # My thinking: build the answer letter by letter.
        # A digit wipes out the closest letter before it
        # — which is just the last letter I kept — so I
        # pop it off and drop the digit too.
        kept = []
        for ch in s:
            if ch.isdigit():
                kept.pop()
            else:
                kept.append(ch)
        return "".join(kept)
