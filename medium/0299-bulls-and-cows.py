# LeetCode 299. Bulls and Cows — Medium
# https://leetcode.com/problems/bulls-and-cows/
# Submission 2198735158 — Accepted, Python3
#
# My thinking: bulls are the positions that already
# match. For the rest I count how often each digit
# appears in the secret and in the guess — every
# digit both sides share, up to the smaller count,
# is a cow.

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        secret_counts = {}
        guess_counts = {}
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                secret_counts[s] = secret_counts.get(s, 0) + 1
                guess_counts[g] = guess_counts.get(g, 0) + 1
        cows = sum(
            min(secret_counts.get(digit, 0), guess_counts.get(digit, 0))
            for digit in secret_counts
        )
        return f"{bulls}A{cows}B"
