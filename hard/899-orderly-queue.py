class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        # My thinking: with two or more movable letters I can sort
        # freely, but with one I can only rotate — so pick the best
        # rotation I can reach.
        if k > 1:
            return "".join(sorted(s))
        best = s
        for i in range(1, len(s)):
            rotated = s[i:] + s[:i]
            if rotated < best:
                best = rotated
        return best
