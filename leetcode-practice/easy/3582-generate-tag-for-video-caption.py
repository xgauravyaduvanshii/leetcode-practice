# 3582. Generate Tag for Video Caption (Easy)
# https://leetcode.com/problems/generate-tag-for-video-caption/
# Submission 2200029009 — Accepted, Python3
class Solution:
    def generateTag(self, caption: str) -> str:
        # My thinking: split the caption into words.
        # The first word stays lowercase, every later
        # word gets its first letter capitalised. Stick
        # a '#' in front, keep only letters, and cut
        # the whole thing to 100 characters. A caption
        # with no words at all is just '#'.
        words = caption.split()
        if not words:
            return "#"
        tag = "#" + words[0].lower()
        for word in words[1:]:
            tag += word.capitalize()
        return tag[:100]
