# LeetCode 91. Decode Ways — Medium
# https://leetcode.com/problems/decode-ways/
# Submission 2203968598 — Accepted, Python3
#
# My thinking: I walk the string left to right, keeping one number —
# how many ways the prefix so far can be decoded. At each position I
# look at the current digit alone and at the last two digits together.
# A single digit decodes on its own only when it is not '0', because
# '0' has no letter of its own. A pair decodes as one letter only when
# it is between 10 and 26, so '06' is never a pair and '27' is not
# either. I add the single-digit ways when the digit is valid and the
# pair ways when the pair is valid, carrying just the last two counts
# forward instead of a whole table. One pass, constant space.

class Solution:
    def numDecodings(self, s: str) -> int:
        # ways for the empty prefix, and for the first character
        prev2, prev1 = 1, 0 if s[0] == '0' else 1
        for i in range(1, len(s)):
            current = 0
            # decode s[i] on its own, only if it is not '0'
            if s[i] != '0':
                current += prev1
            # decode s[i-1:i+1] as one letter, only for 10..26
            two_digit = int(s[i - 1:i + 1])
            if 10 <= two_digit <= 26:
                current += prev2
            prev2, prev1 = prev1, current
        return prev1
