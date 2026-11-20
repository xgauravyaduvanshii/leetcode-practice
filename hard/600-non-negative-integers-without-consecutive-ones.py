class Solution:
    def findIntegers(self, n: int) -> int:
        # My thinking: count valid numbers by their bits — a 0 can be
        # followed by anything, a 1 only by a 0 — so the counts grow
        # like Fibonacci, and a walk down n's bits adds the branches
        # we skip.
        fib = [1, 2]
        while fib[-1] <= n:
            fib.append(fib[-1] + fib[-2])
        result = 0
        prev_bit = 0
        for i in range(len(bin(n)) - 2, -1, -1):
            if n & (1 << i):
                result += fib[i]
                if prev_bit:
                    return result
                prev_bit = 1
            else:
                prev_bit = 0
        return result + 1
