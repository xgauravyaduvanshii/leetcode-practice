# LeetCode 2671. Frequency Tracker — Medium
# https://leetcode.com/problems/frequency-tracker/
# Submission 2205116429 — Accepted, Python3
#
# My thinking: keep two maps — how many times each number has
# appeared, and how many numbers currently sit at each
# frequency. add/deleteOne move one number between frequency
# buckets; hasFrequency just checks whether its bucket is
# non-empty.
from collections import defaultdict


class FrequencyTracker:
    def __init__(self):
        self.freq = defaultdict(int)
        self.by_freq = defaultdict(int)

    def add(self, number: int) -> None:
        old = self.freq[number]
        if old > 0:
            self.by_freq[old] -= 1
        self.freq[number] = old + 1
        self.by_freq[old + 1] += 1

    def deleteOne(self, number: int) -> None:
        old = self.freq[number]
        if old == 0:
            return
        self.by_freq[old] -= 1
        self.freq[number] = old - 1
        if old - 1 > 0:
            self.by_freq[old - 1] += 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.by_freq[frequency] > 0
