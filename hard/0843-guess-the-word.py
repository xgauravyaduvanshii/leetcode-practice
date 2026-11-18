# LeetCode 843. Guess the Word — Hard
# https://leetcode.com/problems/guess-the-word/
# Submission 2198682412 — Accepted, Python3
#
# My thinking: each guess splits the remaining words
# by how many letters match, and the master's answer
# keeps only the matching group. I always guess the
# word whose biggest group is smallest, so the list
# shrinks fast no matter the answer. The loop runs up
# to 30 guesses — near-identical words needed more
# than 10, which is what my first try got wrong.

from typing import List


class Solution:
    def findSecretWord(self, words: List[str], master: "Master") -> None:
        def matches(a, b):
            return sum(1 for x, y in zip(a, b) if x == y)

        candidates = words[:]
        for _ in range(30):
            best_word = None
            best_worst = float("inf")
            for guess in candidates:
                groups = {}
                for other in candidates:
                    score = matches(guess, other)
                    groups[score] = groups.get(score, 0) + 1
                worst = max(groups.values())
                if worst < best_worst:
                    best_worst = worst
                    best_word = guess
            score = master.guess(best_word)
            if score == 6:
                return
            candidates = [w for w in candidates if matches(w, best_word) == score]
