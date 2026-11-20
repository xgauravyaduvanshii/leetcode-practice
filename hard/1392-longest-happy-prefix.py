class Solution:
    def longestPrefix(self, s: str) -> str:
        # My thinking: the longest happy prefix is the longest
        # border of the string — the prefix function from the
        # Knuth-Morris-Pratt scan finds it in one pass.
        n = len(s)
        pi = [0] * n
        for i in range(1, n):
            j = pi[i - 1]
            while j > 0 and s[i] != s[j]:
                j = pi[j - 1]
            if s[i] == s[j]:
                j += 1
            pi[i] = j
        return s[:pi[n - 1]]
