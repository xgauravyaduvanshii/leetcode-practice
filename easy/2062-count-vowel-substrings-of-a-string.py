# LeetCode 2062. Count Vowel Substrings of a String — Easy
# https://leetcode.com/problems/count-vowel-substrings-of-a-string/
# Submission 2197611398 — Accepted, Python3
#
# My thinking: I start a substring at every position
# and extend it while the characters are vowels,
# collecting the vowels I have seen. As soon as all
# five vowels have appeared, this substring and
# every longer extension of it (until a consonant)
# count.

class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = set('aeiou')
        count = 0
        n = len(word)
        for i in range(n):
            seen = set()
            for j in range(i, n):
                if word[j] not in vowels:
                    break
                seen.add(word[j])
                if len(seen) == 5:
                    count += 1
        return count
