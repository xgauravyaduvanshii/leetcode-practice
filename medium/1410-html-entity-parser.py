# LeetCode 1410. HTML Entity Parser — Medium
# https://leetcode.com/problems/html-entity-parser/
# Submission 2199054402 — Accepted, Python3
#
# My thinking: each named entity becomes its
# character with a plain text replacement. The
# ampersand goes last, so an entity written out
# as text is not decoded twice.

class Solution:
    def entityParser(self, text: str) -> str:
        for entity, char in [("&quot;", '"'), ("&apos;", "'"), ("&gt;", ">"), ("&lt;", "<"), ("&frasl;", "/"), ("&amp;", "&")]:
            text = text.replace(entity, char)
        return text
