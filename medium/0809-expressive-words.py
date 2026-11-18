# LeetCode 809. Expressive Words — Medium
# https://leetcode.com/problems/expressive-words/
# Submission 2198943705 — Accepted, Python3
#
# My thinking: I compress both strings into runs
# of the same letter. A word can stretch to the
# target when the letters line up and every run
# is either exactly the same length or can grow
# to a run of three or more.

from typing import List


class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def groups(text):
            result = []
            i = 0
            while i < len(text):
                j = i
                while j < len(text) and text[j] == text[i]:
                    j += 1
                result.append((text[i], j - i))
                i = j
            return result

        target = groups(s)
        stretchy = 0
        for word in words:
            word_groups = groups(word)
            if len(word_groups) != len(target):
                continue
            ok = True
            for (ch1, count1), (ch2, count2) in zip(word_groups, target):
                if ch1 != ch2 or count2 < count1 or (count2 < 3 and count2 != count1):
                    ok = False
                    break
            if ok:
                stretchy += 1
        return stretchy
