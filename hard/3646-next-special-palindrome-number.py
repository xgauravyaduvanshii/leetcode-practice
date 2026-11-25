# LeetCode 3646. Next Special Palindrome Number — Hard
# https://leetcode.com/problems/next-special-palindrome-number/
# Submission 2202928232 — Accepted, Python3
from collections import Counter
from itertools import combinations
from typing import List


class Solution:
    def nextSpecialPalindrome(self, n: int) -> int:
        # My thinking: a special number never contains 0 (0 would
        # have to appear exactly 0 times) and a digit d appears
        # exactly d times, so the digit set is a subset of 1..9
        # with at most one odd digit (a palindrome can have only
        # one digit with an odd count). There are only 96 such
        # subsets, so I try each one: its length is fixed, its
        # palindrome is fixed by its left half, and for the length
        # matching n I build the smallest half that beats n digit
        # by digit, preferring to stay equal to n while a valid
        # completion still exists, and otherwise taking the
        # smallest larger digit. The answer is the smallest
        # candidate over all subsets.
        s = str(n)
        digits = len(s)
        best = None

        odds = [1, 3, 5, 7, 9]
        evens = [2, 4, 6, 8]

        def smallest_palindrome(half, middle):
            left = "".join(str(d) for d in half)
            mid = str(middle) if middle is not None else ""
            return int(left + mid + left[::-1])

        def smallest_half_above(half_counts, middle, L):
            # Smallest palindrome of this digit set that is > s,
            # or None. half_counts maps digit -> count in the left
            # half; middle is the centre digit (odd length only).
            # The palindrome is fixed by its first half t (length
            # m); t > s[:m] already means the palindrome beats s,
            # while t == s[:m] needs the mirrored half to beat
            # s[m:]. I build t left to right, staying equal to s
            # while a valid completion exists, else taking the
            # smallest larger digit.
            m = (L + 1) // 2
            odd = L % 2 == 1

            def suffix_can_beat(rem, tgt_half, mid_t):
                # Can the remaining half digits fill the half
                # positions so the half beats tgt_half, or equals
                # it with the middle digit beating mid_t?
                counts = dict(rem)
                for ch in tgt_half:
                    t = ord(ch) - 48
                    for d in range(t + 1, 10):
                        if counts.get(d, 0) > 0:
                            return True
                    if counts.get(t, 0) == 0:
                        return False
                    counts[t] -= 1
                if mid_t is None:
                    return False
                return middle > mid_t

            def finish(prefix_t, rem, greater_pos):
                # Complete t after a digit larger than s was taken
                # at greater_pos: smallest arrangement of what is
                # left, middle digit last when the length is odd
                # and it is not already in place.
                rest = []
                for d in sorted(rem):
                    if rem[d] > 0:
                        rest.extend([d] * rem[d])
                out = list(prefix_t) + rest
                if odd and len(out) == m - 1:
                    out.append(middle)
                return out

            remaining = Counter()
            for d, c in half_counts.items():
                if c:
                    remaining[d] = c
            t = []
            for pos in range(m):
                if odd and pos == m - 1:
                    cands = [middle]
                else:
                    cands = sorted(d for d in remaining if remaining[d] > 0)
                placed = False
                for c in cands:
                    if c < ord(s[pos]) - 48:
                        continue
                    if c > ord(s[pos]) - 48:
                        # A larger digit here already beats s.
                        rem = remaining.copy()
                        if not (odd and pos == m - 1):
                            rem[c] -= 1
                        t = finish(t + [c], rem, pos)
                        return int(
                            "".join(str(d) for d in t)
                            + "".join(str(d) for d in t[: m - 1 if odd else m][::-1])
                        )
                    # c equals s[pos]: stay equal if a completion
                    # can still beat s.
                    rem = remaining.copy()
                    if not (odd and pos == m - 1):
                        rem[c] -= 1
                    if odd:
                        tgt_half = s[pos + 1:m - 1]
                        mid_t = ord(s[m - 1]) - 48
                    else:
                        tgt_half = s[pos + 1:m]
                        mid_t = None
                    if suffix_can_beat(rem, tgt_half, mid_t):
                        t.append(c)
                        remaining = rem
                        placed = True
                        break
                    # The only equal completion is tgt_half itself
                    # (plus the middle): check its mirror.
                    if Counter(rem.elements()) == Counter(tgt_half) and (
                        mid_t is None or middle == mid_t
                    ):
                        t_full = (
                            t
                            + [c]
                            + [ord(ch) - 48 for ch in tgt_half]
                        )
                        if odd and pos < m - 1:
                            t_full.append(middle)
                        left = t_full if not odd else t_full[:-1]
                        mirror = "".join(str(d) for d in left[::-1])
                        if mirror > s[m:]:
                            t.append(c)
                            remaining = rem
                            placed = True
                            break
                if not placed:
                    return None
            # Every position stayed equal to s and the mirror check
            # passed, so t is complete and its palindrome beats s.
            left = t if not odd else t[:-1]
            return int(
                "".join(str(d) for d in t)
                + "".join(str(d) for d in left[::-1])
            )

        # Subsets of 1..9 with at most one odd digit.
        subsets = []
        for r in range(0, 5):
            for ev in combinations(evens, r):
                subsets.append(list(ev))
                for o in odds:
                    subsets.append(list(ev) + [o])

        for subset in subsets:
            L = sum(subset)
            if L < digits:
                continue
            half_counts = {d: d // 2 for d in subset}
            middle = None
            for d in subset:
                if d % 2 == 1:
                    middle = d
            if L > digits:
                cand = smallest_palindrome(
                    sorted(
                        d for d, c in half_counts.items() for _ in range(c)
                    ),
                    middle,
                )
                best = cand if best is None else min(best, cand)
            else:
                cand = smallest_half_above(half_counts, middle, L)
                if cand is not None:
                    best = cand if best is None else min(best, cand)
        return best
