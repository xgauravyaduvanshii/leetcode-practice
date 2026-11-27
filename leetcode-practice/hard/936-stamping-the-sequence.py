class Solution:
    def movesToStamp(self, stamp: str, target: str) -> list[int]:
        # My thinking: work backwards — a stamp position can be
        # erased if it matches the stamp wherever it is not already
        # blank, so erase greedily and reverse the order.
        m, n = len(stamp), len(target)
        target = list(target)
        stamped = [False] * (n - m + 1)
        moves = []
        total_stamped = 0
        while total_stamped < n:
            changed = False
            for i in range(n - m + 1):
                if stamped[i]:
                    continue
                matched = 0
                ok = True
                for j in range(m):
                    c = target[i + j]
                    if c == "?":
                        continue
                    if c != stamp[j]:
                        ok = False
                        break
                    matched += 1
                if ok and matched > 0:
                    stamped[i] = True
                    changed = True
                    moves.append(i)
                    for j in range(m):
                        if target[i + j] != "?":
                            target[i + j] = "?"
                            total_stamped += 1
            if not changed:
                return []
        return moves[::-1]
