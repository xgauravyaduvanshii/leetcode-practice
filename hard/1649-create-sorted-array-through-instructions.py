class Solution:
    def createSortedArray(self, instructions: list[int]) -> int:
        # My thinking: each new number costs the smaller of
        # how many are already below it and how many are
        # above it — a Fenwick tree keeps both counts cheap.
        MOD = 10 ** 9 + 7
        vals = sorted(set(instructions))
        comp = {v: i + 1 for i, v in enumerate(vals)}
        n = len(vals)
        bit = [0] * (n + 2)

        def add(i, delta):
            while i <= n:
                bit[i] += delta
                i += i & -i

        def prefix(i):
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & -i
            return s

        total = 0
        cost = 0
        for x in instructions:
            i = comp[x]
            smaller = prefix(i - 1)
            greater = total - prefix(i)
            cost = (cost + min(smaller, greater)) % MOD
            add(i, 1)
            total += 1
        return cost
