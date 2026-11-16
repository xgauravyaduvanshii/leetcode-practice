# LeetCode 2000. Reverse Prefix of Word — Easy
# https://leetcode.com/problems/reverse-prefix-of-word/
# Submission 2197608291 — Accepted, Python3
#
# My thinking: I find the first occurrence of the
# given character. If it is not there, the word
# stays as it is. Otherwise I reverse everything up
# to and including that character and keep the rest.

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        i = word.find(ch)
        if i == -1:
            return word
        return word[:i + 1][::-1] + word[i + 1:]
