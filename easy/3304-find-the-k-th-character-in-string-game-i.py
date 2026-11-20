# 3304. Find the K-th Character in String Game I (Easy)
# https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/
# Submission 2200002679 — Accepted, Python3
class Solution:
    def kthCharacter(self, k: int) -> str:
        # My thinking: the word grows by copying itself
        # with every letter moved one step forward. I
        # keep growing it until it is long enough, then
        # read the k-th letter.
        word = "a"
        while len(word) < k:
            word += "".join(chr(ord(ch) + 1) if ch != "z" else "a" for ch in word)
        return word[k - 1]
