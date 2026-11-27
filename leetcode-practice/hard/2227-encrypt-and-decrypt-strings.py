# LeetCode 2227. Encrypt and Decrypt Strings — Hard
# https://leetcode.com/problems/encrypt-and-decrypt-strings/
# Submission 2201628492 — Accepted, Python3
#
# My thinking: encryption is fixed — every
# letter always becomes the same two — so a
# word's encrypted form is fixed too, and
# decrypting is just counting how many
# dictionary words share that form.

from collections import Counter


class Encrypter:
    def __init__(self, keys: list[str], values: list[str], dictionary: list[str]):
        self.mp = dict(zip(keys, values))
        self.enc_count = Counter()
        for word in dictionary:
            enc = self.encrypt(word)
            if enc:
                self.enc_count[enc] += 1

    def encrypt(self, word1: str) -> str:
        out = []
        for c in word1:
            if c not in self.mp:
                return ""
            out.append(self.mp[c])
        return "".join(out)

    def decrypt(self, word2: str) -> int:
        return self.enc_count.get(word2, 0)
