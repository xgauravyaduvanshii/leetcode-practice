class Solution:
    def maximumRequests(self, n: int, requests: list[list[int]]) -> int:
        # My thinking: a set of moves works when every building
        # sends as many people as it receives — so try the
        # biggest sets first and keep the first one that balances.
        m = len(requests)
        best = 0
        for mask in range(1 << m):
            cnt = bin(mask).count("1")
            if cnt <= best:
                continue
            bal = [0] * n
            for i in range(m):
                if mask >> i & 1:
                    a, b = requests[i]
                    bal[a] -= 1
                    bal[b] += 1
            if all(v == 0 for v in bal):
                best = cnt
        return best
