# LeetCode 345. Reverse Vowels of a String — Easy
# https://leetcode.com/problems/reverse-vowels-of-a-string/
# Submission 2197465353 — Accepted, Python3
#
# My thinking: same two-pointer idea as reversing a
# string, but I only swap vowels. Each pointer skips
# past consonants until it finds a vowel, then the
# two vowels swap places.

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        chars = list(s)
        left, right = 0, len(chars) - 1
        while left < right:
            while left < right and chars[left] not in vowels:
                left += 1
            while left < right and chars[right] not in vowels:
                right -= 1
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1
        return "".join(chars)
