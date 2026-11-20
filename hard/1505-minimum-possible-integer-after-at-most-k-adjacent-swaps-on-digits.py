from collections import deque


class Solution:
    def minInteger(self, num: str, k: int) -> str:
        # My thinking: at each step, pull forward the smallest
        # digit still within reach — a Fenwick tree tracks
        # which digits are left and how far each one has to
        # travel.
        n = len(num)
        queues = [deque() for _ in range(10)]
        for i, c in enumerate(num):
            queues[int(c)].append(i)
        bit = [0] * (n + 1)

        def bit_add(i, delta):
            i += 1
            while i <= n:
                bit[i] += delta
                i += i & -i

        def bit_sum(i):
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & -i
            return s

        for i in range(n):
            bit_add(i, 1)
        out = []
        remaining = k
        for _ in range(n):
            for d in range(10):
                if not queues[d]:
                    continue
                pos = queues[d][0]
                cost = bit_sum(pos)
                if cost <= remaining:
                    out.append(str(d))
                    queues[d].popleft()
                    bit_add(pos, -1)
                    remaining -= cost
                    break
        return "".join(out)
