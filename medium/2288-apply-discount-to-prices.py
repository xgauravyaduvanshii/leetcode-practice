# LeetCode 2288. Apply Discount to Prices — Medium
# https://leetcode.com/problems/apply-discount-to-prices/
# Submission 2204643249 — Accepted, Python3
#
# My thinking: a word is a price only if it starts with '$' followed by
# digits only (a lone '$' or a trailing '$' like '5$' is not a price).
# For a price I work in integer cents — price * (100 - discount) — and
# format dollars and two-digit cents, which avoids any floating-point
# rounding. All other words pass through unchanged.
class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        out = []
        for w in sentence.split(' '):
            if len(w) > 1 and w[0] == '$' and w[1:].isdigit():
                cents = int(w[1:]) * (100 - discount)
                out.append(f"${cents // 100}.{cents % 100:02d}")
            else:
                out.append(w)
        return ' '.join(out)
