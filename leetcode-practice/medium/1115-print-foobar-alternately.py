# LeetCode 1115. Print FooBar Alternately — Medium
# https://leetcode.com/problems/print-foobar-alternately/
# Submission 2199001203 — Accepted, Python3
#
# My thinking: two flags take turns — foo waits
# until bar has finished, prints, then hands
# over; bar does the same back. Foo starts
# because its flag is set first.

import threading


class FooBar:
    def __init__(self, n):
        self.n = n
        self.foo_done = threading.Event()
        self.bar_done = threading.Event()
        self.bar_done.set()

    def foo(self, printFoo):
        for _ in range(self.n):
            self.bar_done.wait()
            self.bar_done.clear()
            printFoo()
            self.foo_done.set()

    def bar(self, printBar):
        for _ in range(self.n):
            self.foo_done.wait()
            self.foo_done.clear()
            printBar()
            self.bar_done.set()
