# LeetCode 2645. Minimum Additions to Make Valid String — Medium
# https://leetcode.com/problems/minimum-additions-to-make-valid-string/
# Submission 2205109625 — Accepted, Python3
#
# My thinking: a valid string is just "abc" repeated, so walk
# the word against that cycle. Whenever the next letter is not
# the one the cycle expects, an insertion is forced — count
# it and advance the cycle. After the last letter, finish the
# open "abc" group.
class Solution:
    def addMinimum(self, word: str) -> int:
        need = 0
        expect = 0  # 0 -> 'a', 1 -> 'b', 2 -> 'c'
        for ch in word:
            cur = ord(ch) - 97
            while cur != expect:
                need += 1
                expect = (expect + 1) % 3
            expect = (expect + 1) % 3
        need += (3 - expect) % 3
        return need
