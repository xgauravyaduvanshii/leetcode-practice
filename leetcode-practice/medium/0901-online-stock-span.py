# LeetCode 901. Online Stock Span — Medium
# https://leetcode.com/problems/online-stock-span/
# Submission 2198965910 — Accepted, Python3
#
# My thinking: I keep a stack of past prices
# with their spans. A new price swallows every
# span at or below it, and the span I return is
# one plus everything swallowed.

class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        self.stack.append((price, span))
        return span
