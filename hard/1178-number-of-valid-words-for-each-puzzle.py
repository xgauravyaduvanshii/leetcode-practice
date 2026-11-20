from collections import Counter


class Solution:
    def findNumOfValidWords(self, words: list[str], puzzles: list[str]) -> list[int]:
        # My thinking: a word fits when its letters are all in the
        # puzzle and it uses the first letter — count words by
        # letter mask, then walk the puzzle's sub-masks.
        word_counts = Counter()
        for word in words:
            mask = 0
            for ch in set(word):
                mask |= 1 << (ord(ch) - ord("a"))
            word_counts[mask] += 1
        result = []
        for puzzle in puzzles:
            puzzle_mask = 0
            for ch in puzzle:
                puzzle_mask |= 1 << (ord(ch) - ord("a"))
            first = 1 << (ord(puzzle[0]) - ord("a"))
            total = 0
            submask = puzzle_mask
            while submask:
                if submask & first:
                    total += word_counts.get(submask, 0)
                submask = (submask - 1) & puzzle_mask
            result.append(total)
        return result
