# LeetCode 3474. Lexicographically Smallest Generated String — Hard
# https://leetcode.com/problems/lexicographically-smallest-generated-string/
# Submission 2202664110 — Accepted 742/742, Python3
#
# My thinking: every 'T' in str1 pins a whole copy of str2 into the word,
# so I write those in first and give up if two of them disagree on a
# position. The remaining free positions default to 'a'. Then I walk the
# 'F' windows left to right: if a window still spells str2, I change its
# rightmost free position to the smallest letter different from str2's
# letter there ('b' when str2 has 'a', else 'a'). Changing the rightmost
# free spot keeps the word as small as possible, and once a window is made
# different it stays different, because the changed position is fixed from
# then on. If a window that spells str2 has no free position left, there
# is no valid word at all.

class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        word = [None] * (n + m - 1)
        for i, ch in enumerate(str1):
            if ch == "T":
                for j in range(m):
                    if word[i + j] is None:
                        word[i + j] = str2[j]
                    elif word[i + j] != str2[j]:
                        return ""
        for i, ch in enumerate(str1):
            if ch == "F":
                cur = "".join(
                    word[i + j] if word[i + j] is not None else "a" for j in range(m)
                )
                if cur == str2:
                    for j in range(m - 1, -1, -1):
                        if word[i + j] is None:
                            word[i + j] = "b" if str2[j] == "a" else "a"
                            break
                    else:
                        return ""
        return "".join(word[i] if word[i] is not None else "a" for i in range(n + m - 1))
