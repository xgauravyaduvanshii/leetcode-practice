# LeetCode 1117. Building H2O — Medium
# https://leetcode.com/problems/building-h2o/
# Submission 2199001604 — Accepted, Python3
#
# My thinking: a molecule needs two hydrogens
# before its oxygen. Hydrogens wait once two
# are already in, and the oxygen waits until
# both have arrived — then it resets the count
# for the next molecule.

import threading


class H2O:
    def __init__(self):
        self.condition = threading.Condition()
        self.hydrogen_count = 0

    def hydrogen(self, releaseHydrogen):
        with self.condition:
            while self.hydrogen_count == 2:
                self.condition.wait()
            releaseHydrogen()
            self.hydrogen_count += 1
            if self.hydrogen_count == 2:
                self.condition.notify_all()

    def oxygen(self, releaseOxygen):
        with self.condition:
            while self.hydrogen_count < 2:
                self.condition.wait()
            releaseOxygen()
            self.hydrogen_count = 0
            self.condition.notify_all()
