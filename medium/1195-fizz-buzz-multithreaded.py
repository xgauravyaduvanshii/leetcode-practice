# LeetCode 1195. Fizz Buzz Multithreaded — Medium
# https://leetcode.com/problems/fizz-buzz-multithreaded/
# Submission 2199011727 — Accepted, Python3
#
# My thinking: one shared counter decides whose
# turn it is. Each thread waits until the
# counter hits a number it owns, prints, moves
# the counter on, and wakes the others.

import threading


class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.current = 1
        self.lock = threading.Lock()
        self.condition = threading.Condition(self.lock)

    def fizz(self, printFizz):
        while True:
            with self.condition:
                while self.current <= self.n and (self.current % 3 != 0 or self.current % 5 == 0):
                    self.condition.wait()
                if self.current > self.n:
                    self.condition.notify_all()
                    return
                printFizz()
                self.current += 1
                self.condition.notify_all()

    def buzz(self, printBuzz):
        while True:
            with self.condition:
                while self.current <= self.n and (self.current % 5 != 0 or self.current % 3 == 0):
                    self.condition.wait()
                if self.current > self.n:
                    self.condition.notify_all()
                    return
                printBuzz()
                self.current += 1
                self.condition.notify_all()

    def fizzbuzz(self, printFizzBuzz):
        while True:
            with self.condition:
                while self.current <= self.n and self.current % 15 != 0:
                    self.condition.wait()
                if self.current > self.n:
                    self.condition.notify_all()
                    return
                printFizzBuzz()
                self.current += 1
                self.condition.notify_all()

    def number(self, printNumber):
        while True:
            with self.condition:
                while self.current <= self.n and (self.current % 3 == 0 or self.current % 5 == 0):
                    self.condition.wait()
                if self.current > self.n:
                    self.condition.notify_all()
                    return
                printNumber(self.current)
                self.current += 1
                self.condition.notify_all()
