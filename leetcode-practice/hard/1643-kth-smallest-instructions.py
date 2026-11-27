import math


class Solution:
    def kthSmallestPath(self, destination: list[int], k: int) -> str:
        # My thinking: 'H' comes before 'V', so at each step
        # count how many paths start with 'H' — if k fits
        # inside, take it, otherwise take 'V' and skip past.
        # destination is (row, column): 'V' moves down a row,
        # 'H' moves right a column.
        v, h = destination
        res = []
        while h > 0 or v > 0:
            if h == 0:
                res.append("V")
                v -= 1
            elif v == 0:
                res.append("H")
                h -= 1
            else:
                cnt = math.comb(h + v - 1, h - 1)
                if k <= cnt:
                    res.append("H")
                    h -= 1
                else:
                    res.append("V")
                    k -= cnt
                    v -= 1
        return "".join(res)
