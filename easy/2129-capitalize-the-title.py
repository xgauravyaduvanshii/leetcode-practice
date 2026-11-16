# LeetCode 2129. Capitalize the Title — Easy
# https://leetcode.com/problems/capitalize-the-title/
# Submission 2197614247 — Accepted, Python3
#
# My thinking: words of length 1 or 2 become all
# lowercase. Longer words get their first letter
# capitalised and the rest lowercase.

class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words = []
        for w in title.split():
            if len(w) > 2:
                words.append(w[0].upper() + w[1:].lower())
            else:
                words.append(w.lower())
        return ' '.join(words)
