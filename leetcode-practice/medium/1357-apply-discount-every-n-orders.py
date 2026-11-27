# LeetCode 1357. Apply Discount Every n Orders — Medium
# https://leetcode.com/problems/apply-discount-every-n-orders/
# Submission 2199038056 — Accepted, Python3
#
# My thinking: the bill is the price of every
# item times its amount. Every nth customer
# gets the same bill with the discount taken
# off.

from typing import List


class Cashier:
    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.discount = discount
        self.prices = dict(zip(products, prices))
        self.count = 0

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.count += 1
        total = sum(self.prices[p] * a for p, a in zip(product, amount))
        if self.count % self.n == 0:
            total *= (100 - self.discount) / 100
        return total
