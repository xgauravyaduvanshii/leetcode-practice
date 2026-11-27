# LeetCode 4105. Repeated String Match II — Hard
# https://leetcode.com/problems/repeated-string-match-ii/
# Submission 2203733695 — Accepted, Python3
import math


class Solution:
    def repeatedStringMatch(self, a: str, b: str, x: int, y: int) -> bool:
        # My thinking: the target is b repeated y times,
        # sitting inside a repeated x times. Any match
        # must start at some offset inside one copy of a,
        # so only starting offsets 0..|a|-1 need checking.
        # At a fixed offset, the pair of indices
        # ((off + t) % |a|, t % |b|) repeats with period
        # lcm(|a|, |b|), so comparing the first
        # min(L, lcm) characters decides the whole match:
        # if they all line up, the pattern repeats
        # forever and the rest of the match follows.
        # If the target is longer than the whole repeated
        # a, it can never fit, so return False early.
        A = len(a)
        B = len(b)
        N = A * x
        L = B * y
        if L > N:
            return False
        lcm = A * B // math.gcd(A, B)
        limit = min(L, lcm)
        for off in range(A):
            if off + L > N:
                break
            ok = True
            for t in range(limit):
                if a[(off + t) % A] != b[t % B]:
                    ok = False
                    break
            if ok:
                return True
        return False
