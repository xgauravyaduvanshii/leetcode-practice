# LeetCode 423. Reconstruct Original Digits from English — Medium
# https://leetcode.com/problems/reconstruct-original-digits-from-english/
# Submission 2198786736 — Accepted, Python3
#
# My thinking: some digits own a letter no other
# digit uses — z for zero, w for two, u for four, x
# for six, g for eight. Counting those gives five
# digits directly, and the rest follow by removing
# what those digits already explain.

from collections import Counter


class Solution:
    def originalDigits(self, s: str) -> str:
        counts = Counter(s)
        digits = [0] * 10
        digits[0] = counts["z"]  # zero
        digits[2] = counts["w"]  # two
        digits[4] = counts["u"]  # four
        digits[6] = counts["x"]  # six
        digits[8] = counts["g"]  # eight
        digits[3] = counts["h"] - digits[8]  # three, h also in eight
        digits[5] = counts["f"] - digits[4]  # five, f also in four
        digits[7] = counts["s"] - digits[6]  # seven, s also in six
        digits[1] = counts["o"] - digits[0] - digits[2] - digits[4]  # one
        digits[9] = counts["i"] - digits[5] - digits[6] - digits[8]  # nine
        return "".join(str(d) * digits[d] for d in range(10))
