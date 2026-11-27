class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        # My thinking: the top bit can only flip when the bit
        # below it is set and everything under it is clear —
        # so clear the top bit, then fix the rest backwards.
        if n == 0:
            return 0
        k = n.bit_length() - 1
        return (1 << (k + 1)) - 1 - self.minimumOneBitOperations(n - (1 << k))
