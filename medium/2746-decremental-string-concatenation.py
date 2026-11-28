# LeetCode 2746. Decremental String Concatenation — Medium
# https://leetcode.com/problems/decremental-string-concatenation/
# Submission 2205237107 — Accepted, Python3
#
# My thinking: only the first and last characters of the
# string built so far matter, so keep a DP over those two
# letters: dp[first][last] is the shortest length achievable
# after using the words seen so far. Each new word is either
# appended (saving 1 when its first letter matches the current
# last letter) or prepended (saving 1 when its last letter
# matches the current first letter). The answer is the best
# entry after the last word.
class Solution:
    def minimizeConcatenatedLength(self, words: list[str]) -> int:
        INF = 10 ** 9
        dp = [[INF] * 26 for _ in range(26)]
        first, last = ord(words[0][0]) - 97, ord(words[0][-1]) - 97
        dp[first][last] = len(words[0])
        for w in words[1:]:
            f, l = ord(w[0]) - 97, ord(w[-1]) - 97
            ndp = [[INF] * 26 for _ in range(26)]
            for a in range(26):
                for b in range(26):
                    if dp[a][b] == INF:
                        continue
                    # Append w after the current string.
                    ndp[a][l] = min(ndp[a][l], dp[a][b] + len(w) - (b == f))
                    # Prepend w before the current string.
                    ndp[f][b] = min(ndp[f][b], dp[a][b] + len(w) - (l == a))
            dp = ndp
        return min(min(row) for row in dp)
