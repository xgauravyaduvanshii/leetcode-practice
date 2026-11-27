class Solution:
    def countOrders(self, n: int) -> int:
        # My thinking: with i orders placed, the next pickup
        # can go in any of 2i+1 gaps and its delivery in any
        # of the i+1 gaps after it — multiply it out.
        MOD = 10 ** 9 + 7
        total = 1
        for i in range(1, n + 1):
            total = total * i * (2 * i - 1) % MOD
        return total
