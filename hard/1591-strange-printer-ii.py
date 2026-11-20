class Solution:
    def isPrintable(self, targetGrid: list[list[int]]) -> bool:
        # My thinking: the last colour printed sits clean on
        # its rectangle — so peel off any colour whose whole
        # rectangle is already gone, and repeat.
        m, n = len(targetGrid), len(targetGrid[0])
        rect = {}
        for i in range(m):
            for j in range(n):
                c = targetGrid[i][j]
                if c not in rect:
                    rect[c] = [i, i, j, j]
                else:
                    r = rect[c]
                    r[0] = min(r[0], i)
                    r[1] = max(r[1], i)
                    r[2] = min(r[2], j)
                    r[3] = max(r[3], j)
        removed = set()
        changed = True
        while changed:
            changed = False
            for c, (r1, r2, c1, c2) in rect.items():
                if c in removed:
                    continue
                ok = True
                for i in range(r1, r2 + 1):
                    for j in range(c1, c2 + 1):
                        if targetGrid[i][j] not in removed and targetGrid[i][j] != c:
                            ok = False
                            break
                    if not ok:
                        break
                if ok:
                    removed.add(c)
                    changed = True
        return len(removed) == len(rect)
