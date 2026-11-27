from fractions import Fraction


class Solution:
    def isRationalEqual(self, s: str, t: str) -> bool:
        # My thinking: expand each decimal into an exact fraction —
        # the repeating tail is a geometric series — then just
        # compare the two fractions.
        def to_fraction(s):
            if "(" in s:
                head, rest = s.split("(")
                repeating = rest[:-1]
            else:
                head, repeating = s, ""
            if "." in head:
                integer, non_repeating = head.split(".")
            else:
                integer, non_repeating = head, ""
            value = Fraction(int(integer or 0))
            for i, ch in enumerate(non_repeating, 1):
                value += Fraction(int(ch), 10 ** i)
            if repeating:
                k = len(non_repeating)
                length = len(repeating)
                value += Fraction(int(repeating), 10 ** k * (10 ** length - 1))
            return value

        return to_fraction(s) == to_fraction(t)
