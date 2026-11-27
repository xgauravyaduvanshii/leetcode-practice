# LeetCode 1114. Print in Order — Easy
# https://leetcode.com/problems/print-in-order/
# Submission 2197557954 — Accepted, Python3
#
# My thinking: I use two locks, both locked to start.
# first() prints and unlocks the first lock, which
# lets second() run; second() prints and unlocks
# the second lock, which lets third() run. No
# matter what order the threads start in, the
# output always comes out first, second, third.

from threading import Lock


class Foo:
    def __init__(self):
        self.first_done = Lock()
        self.second_done = Lock()
        self.first_done.acquire()
        self.second_done.acquire()

    def first(self, printFirst) -> None:
        printFirst()
        self.first_done.release()

    def second(self, printSecond) -> None:
        with self.first_done:
            printSecond()
            self.second_done.release()

    def third(self, printThird) -> None:
        with self.second_done:
            printThird()
