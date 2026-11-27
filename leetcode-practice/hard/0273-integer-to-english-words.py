# LeetCode 273. Integer to English Words — Hard
# https://leetcode.com/problems/integer-to-english-words/
# Submission 2198398239 — Accepted, Python3
#
# My thinking: I split the number into groups of
# three digits from the right — units, thousands,
# millions, billions. Each group is spoken the same
# way: hundreds, then tens and ones, with the teen
# numbers spelled out directly. I skip empty groups
# and tag each spoken group with its scale word.

from typing import List


class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
                "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen",
                "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        thousands = ["", "Thousand", "Million", "Billion"]

        def under_thousand(n: int) -> List[str]:
            words = []
            if n >= 100:
                words.append(ones[n // 100])
                words.append("Hundred")
                n %= 100
            if n >= 20:
                words.append(tens[n // 10])
                if n % 10:
                    words.append(ones[n % 10])
            elif n > 0:
                words.append(ones[n])
            return words

        words = []
        group = 0
        while num > 0:
            chunk = num % 1000
            if chunk:
                chunk_words = under_thousand(chunk)
                if thousands[group]:
                    chunk_words.append(thousands[group])
                words = chunk_words + words
            num //= 1000
            group += 1
        return " ".join(words)
