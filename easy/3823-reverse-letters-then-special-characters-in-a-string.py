# 3823. Reverse Letters Then Special Characters in a String (Easy)
# https://leetcode.com/problems/reverse-letters-then-special-characters-in-a-string/
# Submission 2200069228 — Accepted, Python3
class Solution:
    def reverseByType(self, s: str) -> str:
        # My thinking: letters only swap with letters
        # and special characters only with specials.
        # I reverse each group on its own and put it
        # back into the same kind of spots.
        chars = list(s)
        letter_pos = [i for i, ch in enumerate(s) if ch.isalpha()]
        letters = [s[i] for i in letter_pos][::-1]
        for i, ch in zip(letter_pos, letters):
            chars[i] = ch
        special_pos = [i for i, ch in enumerate(s) if not ch.isalpha()]
        specials = [s[i] for i in special_pos][::-1]
        for i, ch in zip(special_pos, specials):
            chars[i] = ch
        return "".join(chars)
