class Solution:
    def maxValue(self, n: str, x: int) -> str:
        # My thinking: for a positive number, slip x in front of
        # the first smaller digit; for a negative one, in front
        # of the first bigger digit — either way the bigger digit
        # moves to a more valuable place.
        digit = str(x)
        if n[0] != "-":
            for i, ch in enumerate(n):
                if int(ch) < x:
                    return n[:i] + digit + n[i:]
            return n + digit
        for i, ch in enumerate(n[1:], start=1):
            if int(ch) > x:
                return n[:i] + digit + n[i:]
        return n + digit
