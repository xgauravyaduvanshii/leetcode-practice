class Solution:
    def lastSubstring(self, s: str) -> str:
        # My thinking: two candidates race down the string, and
        # the first mismatch kills the smaller one — the skip
        # jumps past every suffix the loser could still win with.
        n = len(s)
        i, j, k = 0, 1, 0
        while j + k < n:
            if s[i + k] == s[j + k]:
                k += 1
            elif s[i + k] < s[j + k]:
                i = max(i + k + 1, j)
                j = i + 1
                k = 0
            else:
                j = j + k + 1
                k = 0
        return s[i:]
