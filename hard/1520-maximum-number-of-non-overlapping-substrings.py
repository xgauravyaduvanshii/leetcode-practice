class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        # My thinking: each letter forces its whole span into
        # one piece — so grow every letter's span until it
        # closes, then take the most pieces that don't touch.
        first = {}
        last = {}
        for i, c in enumerate(s):
            first.setdefault(c, i)
            last[c] = i
        intervals = []
        for c in first:
            lo, hi = first[c], last[c]
            j = lo
            while j <= hi:
                lo = min(lo, first[s[j]])
                hi = max(hi, last[s[j]])
                j += 1
            if lo == first[c]:
                intervals.append((hi, lo))
        intervals.sort()
        out = []
        prev_end = -1
        for hi, lo in intervals:
            if lo > prev_end:
                out.append(s[lo:hi + 1])
                prev_end = hi
        return out
