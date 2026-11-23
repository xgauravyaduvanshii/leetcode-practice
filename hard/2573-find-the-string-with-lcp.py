# LeetCode 2573. Find the String with LCP — Hard
# https://leetcode.com/problems/find-the-string-with-lcp/
# Submission 2201827437 — Accepted, Python3
#
# My thinking: equal prefixes mean
# equal letters, so I tie together every
# pair the matrix says must match, check
# the matrix agrees with itself going
# down the diagonal, and then hand out
# the smallest letters that keep the
# zero entries apart.

class Solution:
    def findTheString(self, lcp: list[list[int]]) -> str:
        n = len(lcp)
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[ra] = rb

        for i in range(n):
            if lcp[i][i] != n - i:
                return ""
            for j in range(n):
                if lcp[i][j] != lcp[j][i]:
                    return ""
                if lcp[i][j] > min(n - i, n - j):
                    return ""
                if lcp[i][j] > 0:
                    union(i, j)
                    if i + 1 < n and j + 1 < n:
                        if lcp[i + 1][j + 1] != lcp[i][j] - 1:
                            return ""
                    elif lcp[i][j] != 1:
                        return ""
        # positions in one group must share a letter; check no group is
        # forced apart by a zero entry
        word = [""] * n
        for i in range(n):
            if word[i]:
                continue
            used = set()
            for j in range(i):
                if word[j] and find(j) != find(i) and lcp[i][j] == 0:
                    used.add(word[j])
            # every member of i's group must also avoid those letters; if a
            # group member already carries one, the matrix is inconsistent
            for j in range(n):
                if find(j) == find(i) and word[j]:
                    if word[j] in used:
                        return ""
            c = "a"
            while c in used:
                c = chr(ord(c) + 1)
            if c > "z":
                return ""
            for j in range(n):
                if find(j) == find(i):
                    word[j] = c
        # final check: two positions with lcp 0 must not share a letter
        for i in range(n):
            for j in range(n):
                if lcp[i][j] == 0 and word[i] == word[j]:
                    return ""
        return "".join(word)
