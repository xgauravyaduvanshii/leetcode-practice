from collections import Counter


class Solution:
    def maxScoreWords(self, words: list[str], letters: list[str], score: list[int]) -> int:
        # My thinking: only 14 words, so try every subset —
        # keep the letters it needs, score it if they fit.
        available = Counter(letters)
        word_counts = [Counter(word) for word in words]
        word_scores = [
            sum(score[ord(ch) - ord("a")] for ch in word) for word in words
        ]
        best = 0
        n = len(words)
        for mask in range(1 << n):
            needed = Counter()
            total = 0
            for i in range(n):
                if mask & (1 << i):
                    needed += word_counts[i]
                    total += word_scores[i]
            if all(needed[ch] <= available[ch] for ch in needed):
                best = max(best, total)
        return best
