class Solution:
    def minInsertions(self, s: str) -> int:
        # My thinking: the insertions needed are whatever is
        # left after the longest palindromic subsequence —
        # which is the longest common subsequence of the
        # string and its reverse.
        n = len(s)
        rev = s[::-1]
        prev = [0] * (n + 1)
        for i in range(1, n + 1):
            cur = [0] * (n + 1)
            for j in range(1, n + 1):
                if s[i - 1] == rev[j - 1]:
                    cur[j] = prev[j - 1] + 1
                else:
                    cur[j] = max(prev[j], cur[j - 1])
            prev = cur
        return n - prev[n]
