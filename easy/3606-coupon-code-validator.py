# 3606. Coupon Code Validator (Easy)
# https://leetcode.com/problems/coupon-code-validator/
# Submission 2200033038 — Accepted, Python3
from typing import List


class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        # My thinking: a coupon counts only when it is
        # active, its code is non-empty and made of
        # letters, digits and underscores, and its
        # business line is one of the four known ones.
        # The survivors come out grouped by business
        # line — electronics, grocery, pharmacy,
        # restaurant — and alphabetically inside each
        # group.
        order = {"electronics": 0, "grocery": 1, "pharmacy": 2, "restaurant": 3}
        valid = []
        for c, b, active in zip(code, businessLine, isActive):
            if not active:
                continue
            if not c:
                continue
            if not all(ch.isalnum() or ch == "_" for ch in c):
                continue
            if b not in order:
                continue
            valid.append((order[b], c))
        return [c for _, c in sorted(valid)]
