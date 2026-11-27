# LeetCode 828. Count Unique Characters of All Substrings of a Given String — Hard
# https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/
# Submission 2198679915 — Accepted, Python3
#
# My thinking: instead of listing substrings I ask
# what each position contributes. A letter at position
# i is the unique one in every substring that starts
# after its previous occurrence and ends before its
# next one — that count is the gap on the left times
# the gap on the right.

class Solution:
    def uniqueLetterString(self, s: str) -> int:
        last_seen = {}
        second_last = {}
        total = 0
        for i, ch in enumerate(s):
            prev = last_seen.get(ch, -1)
            prev_prev = second_last.get(ch, -1)
            total += (i - prev) * (prev - prev_prev)
            second_last[ch] = prev
            last_seen[ch] = i
        n = len(s)
        for ch, prev in last_seen.items():
            prev_prev = second_last[ch]
            total += (n - prev) * (prev - prev_prev)
        return total
