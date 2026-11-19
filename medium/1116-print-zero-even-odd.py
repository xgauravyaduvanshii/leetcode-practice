# LeetCode 1116. Print Zero Even Odd — Medium
# https://leetcode.com/problems/print-zero-even-odd/
# Submission 2199001375 — Accepted, Python3
#
# My thinking: three locks pass the turn around
# — zero prints, then wakes the odd or even
# thread as the number demands, and that thread
# wakes zero back. Zero starts with the turn.

import threading


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.zero_lock = threading.Lock()
        self.even_lock = threading.Lock()
        self.odd_lock = threading.Lock()
        self.even_lock.acquire()
        self.odd_lock.acquire()

    def zero(self, printNumber):
        for i in range(1, self.n + 1):
            self.zero_lock.acquire()
            printNumber(0)
            if i % 2 == 1:
                self.odd_lock.release()
            else:
                self.even_lock.release()

    def even(self, printNumber):
        for i in range(2, self.n + 1, 2):
            self.even_lock.acquire()
            printNumber(i)
            self.zero_lock.release()

    def odd(self, printNumber):
        for i in range(1, self.n + 1, 2):
            self.odd_lock.acquire()
            printNumber(i)
            self.zero_lock.release()
