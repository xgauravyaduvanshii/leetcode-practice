class Solution:
    def longestAwesome(self, s: str) -> int:
        # My thinking: a stretch rearranges into a palindrome
        # when at most one digit appears an odd number of times
        # — so track the parity mask and remember where each
        # mask first showed up.
        first = {0: -1}
        mask = 0
        best = 0
        for i, c in enumerate(s):
            mask ^= 1 << int(c)
            if mask in first:
                best = max(best, i - first[mask])
            for d in range(10):
                other = mask ^ (1 << d)
                if other in first:
                    best = max(best, i - first[other])
            if mask not in first:
                first[mask] = i
        return best
