# LeetCode 2024. Maximize the Confusion of an Exam — Medium
# https://leetcode.com/problems/maximize-the-confusion-of-an-exam/
# Submission 2204140342 — Accepted, Python3
#
# My thinking: I want the longest stretch I can make all T or all F by
# flipping at most k answers, so I try each target letter in turn. With a
# sliding window I grow the right end one step at a time and count how
# many flips the window would need (letters that are not the target).
# Whenever the flips pass k, I shrink the window from the left until it
# is legal again. The widest legal window seen for either target is the
# answer, because any longer stretch would need more than k flips.
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        best = 0
        for target in "TF":
            left = 0
            flips = 0
            for right, ch in enumerate(answerKey):
                if ch != target:
                    flips += 1
                while flips > k:
                    if answerKey[left] != target:
                        flips -= 1
                    left += 1
                best = max(best, right - left + 1)
        return best
