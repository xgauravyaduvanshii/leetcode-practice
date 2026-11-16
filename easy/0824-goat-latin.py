# LeetCode 824. Goat Latin — Easy
# https://leetcode.com/problems/goat-latin/
# Submission 2197531841 — Accepted, Python3
#
# My thinking: I go through the words one by one.
# If a word starts with a vowel, I just add "ma".
# If it starts with a consonant, I move that first
# letter to the end and then add "ma". Either way,
# I add one more "a" than the word's position (the
# first word gets one "a", the second gets two...).

class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = set("aeiouAEIOU")
        words = sentence.split()
        result = []
        for i, word in enumerate(words):
            if word[0] in vowels:
                goat = word + "ma"
            else:
                goat = word[1:] + word[0] + "ma"
            goat += "a" * (i + 1)
            result.append(goat)
        return " ".join(result)
