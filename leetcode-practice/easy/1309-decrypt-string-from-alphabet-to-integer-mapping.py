# LeetCode 1309. Decrypt String from Alphabet to Integer Mapping — Easy
# https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/
# Submission 2197569115 — Accepted, Python3
#
# My thinking: I read the string left to right. If
# the character two places ahead is a '#', the
# next two digits together make a letter from 10
# to 26. Otherwise a single digit makes a letter
# from 1 to 9. (Letter 1 is 'a', so I add 96 to the
# number to get the right character.)

class Solution:
    def freqAlphabets(self, s: str) -> str:
        result = []
        i = 0
        while i < len(s):
            if i + 2 < len(s) and s[i + 2] == "#":
                result.append(chr(int(s[i:i + 2]) + 96))
                i += 3
            else:
                result.append(chr(int(s[i]) + 96))
                i += 1
        return "".join(result)
