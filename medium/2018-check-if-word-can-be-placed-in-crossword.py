# LeetCode 2018. Check if Word Can Be Placed In Crossword — Medium
# https://leetcode.com/problems/check-if-word-can-be-placed-in-crossword/
# Submission 2204145087 — Accepted, Python3
#
# My thinking: a word can only sit in a stretch of open cells that is
# exactly as long as the word, with a '#' or the board edge on both
# sides. So I scan every row and every column, cut them into stretches
# separated by '#', and keep only the stretches whose length matches
# the word. A stretch fits if every cell is either blank or already
# holds the matching letter of the word, and I try the word both
# forwards and backwards, which covers placing it left-to-right,
# right-to-left, top-to-bottom and bottom-to-top in one go.

class Solution:
    def placeWordInCrossword(self, board, word):
        def fits(segment):
            if len(segment) != len(word):
                return False
            for cell, ch in zip(segment, word):
                if cell != ' ' and cell != ch:
                    return False
            return True

        def fits_reversed(segment):
            if len(segment) != len(word):
                return False
            for cell, ch in zip(segment, reversed(word)):
                if cell != ' ' and cell != ch:
                    return False
            return True

        m, n = len(board), len(board[0])

        for row in board:
            start = 0
            for j in range(n + 1):
                if j == n or row[j] == '#':
                    segment = row[start:j]
                    if fits(segment) or fits_reversed(segment):
                        return True
                    start = j + 1

        for j in range(n):
            start = 0
            for i in range(m + 1):
                if i == m or board[i][j] == '#':
                    segment = [board[k][j] for k in range(start, i)]
                    if fits(segment) or fits_reversed(segment):
                        return True
                    start = i + 1

        return False


if __name__ == "__main__":
    s = Solution()
    # Example 1
    assert s.placeWordInCrossword(
        [["#", " ", "#"], [" ", " ", "#"], ["#", "c", " "]], "abc") is True
    # Example 2
    assert s.placeWordInCrossword(
        [[" ", "#", "a"], [" ", "#", "c"], [" ", "#", "a"]], "ac") is False
    # Example 3
    assert s.placeWordInCrossword(
        [["#", " ", "#"], [" ", " ", "#"], ["#", " ", "c"]], "ca") is True
    # Extra: word longer than any open stretch
    assert s.placeWordInCrossword([[" ", " "], [" ", " "]], "abc") is False
    # Extra: reversed vertical placement
    assert s.placeWordInCrossword(
        [["a"], [" "], ["#"]], "ba") is True
    print("All sample tests passed.")
