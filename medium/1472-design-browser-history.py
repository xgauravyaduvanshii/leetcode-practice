# LeetCode 1472. Design Browser History — Medium
# https://leetcode.com/problems/design-browser-history/
# Submission 2199857489 — Accepted, Python3
#
# My thinking: I keep the visited pages in a
# list with a pointer at the current one. A
# new visit drops everything ahead and appends;
# back and forward just move the pointer,
# clamped to the ends.

class BrowserHistory:
    def __init__(self, homepage: str):
        self.history = [homepage]
        self.current = 0

    def visit(self, url: str) -> None:
        self.history = self.history[:self.current + 1]
        self.history.append(url)
        self.current += 1

    def back(self, steps: int) -> str:
        self.current = max(0, self.current - steps)
        return self.history[self.current]

    def forward(self, steps: int) -> str:
        self.current = min(len(self.history) - 1, self.current + steps)
        return self.history[self.current]
