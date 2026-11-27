# LeetCode 1226. The Dining Philosophers — Medium
# https://leetcode.com/problems/the-dining-philosophers/
# Submission 2199013600 — Accepted, Python3
#
# My thinking: one lock guards the whole table,
# so only one philosopher eats at a time. They
# pick up both forks, eat, and put both down
# before the next one starts — no deadlock.

import threading


class DiningPhilosophers:
    def __init__(self):
        self.lock = threading.Lock()

    def wantsToEat(self, philosopher, pickLeftFork, pickRightFork, eat, putLeftFork, putRightFork):
        with self.lock:
            pickLeftFork()
            pickRightFork()
            eat()
            putLeftFork()
            putRightFork()
