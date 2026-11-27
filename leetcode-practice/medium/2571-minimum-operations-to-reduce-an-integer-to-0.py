class Solution:
    def minOperations(self, n: int) -> int:
        # My thinking: work from the lowest set bit upward — adding or
        # subtracting the lowest power of two both cost one operation, so
        # take whichever leaves fewer ones: if the two lowest bits are
        # both set, add the lowest power to trigger a carry instead of
        # subtracting it.
        operations = 0
        while n:
            if n & 1:
                if n & 2:
                    n += 1
                else:
                    n -= 1
                operations += 1
            n >>= 1
        return operations
