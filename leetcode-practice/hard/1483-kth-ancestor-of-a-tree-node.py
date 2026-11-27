class TreeAncestor:
    def __init__(self, n: int, parent: list[int]):
        # My thinking: jump up the tree in powers of two —
        # precompute the 1st, 2nd, 4th, 8th... ancestor of
        # every node, then walk k's binary digits upward.
        self.up = [parent[:]]
        j = 1
        while (1 << j) <= n:
            prev = self.up[j - 1]
            self.up.append([prev[prev[i]] if prev[i] != -1 else -1 for i in range(n)])
            j += 1

    def getKthAncestor(self, node: int, k: int) -> int:
        for j in range(len(self.up)):
            if node == -1:
                break
            if k & (1 << j):
                node = self.up[j][node]
        return node
