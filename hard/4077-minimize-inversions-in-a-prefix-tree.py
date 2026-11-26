# LeetCode 4077. Minimize Inversions in a Prefix Tree — Hard
# https://leetcode.com/problems/minimize-inversions-in-a-prefix-tree/
# Submission 2203689842 — Accepted, Python3
class Solution:
    def minInversions(self, words: list[str], target: list[int]) -> int:
        # My thinking: build the prefix tree (trie) of all words.
        # The pre-order traversal is fixed except for the order of
        # each node's children, and each node can be ordered
        # independently — except a word that is a prefix of other
        # words is always visited before its whole subtree. Walking
        # the words in target order, each word's ancestors already
        # processed count as inversions against the still-unseen
        # words in earlier sibling subtrees, which gives a pairwise
        # cost between sibling children; a marked ancestor adds a
        # fixed inversion whenever a later word in target order
        # passes through it. Each node's children are then ordered
        # to minimise their pairwise cost — by direct comparison
        # for two children, or by a subset DP over child orderings
        # (at most 10 children, letters 'a' to 'j') otherwise.
        # Summing the fixed part and every node's best ordering
        # gives the minimum total inversions.
        n = len(words)
        children = [{}]
        mark = [-1]
        paths = []
        for idx, w in enumerate(words):
            node = 0
            path = [0]
            for ch in w:
                nxt = children[node].get(ch)
                if nxt is None:
                    nxt = len(children)
                    children[node][ch] = nxt
                    children.append({})
                    mark.append(-1)
                node = nxt
                path.append(node)
            mark[node] = idx
            paths.append(path)
        m = len(children)
        child_pos = []
        counts = []
        costs = []
        for u in range(m):
            lst = list(children[u].values())
            child_pos.append({v: i for i, v in enumerate(lst)})
            k = len(lst)
            counts.append([0] * k)
            costs.append([[0] * k for _ in range(k)])
        processed = [False] * n
        fixed = 0
        for idx in target:
            path = paths[idx]
            for j in range(len(path) - 1):
                u = path[j]
                v = path[j + 1]
                p = child_pos[u][v]
                cnt = counts[u]
                row = costs[u][p]
                for q in range(len(cnt)):
                    if q != p:
                        row[q] += cnt[q]
                mu = mark[u]
                if mu != -1 and not processed[mu]:
                    fixed += 1
            for j in range(len(path) - 1):
                u = path[j]
                v = path[j + 1]
                counts[u][child_pos[u][v]] += 1
            processed[idx] = True
        total = fixed
        INF = 10 ** 18
        for u in range(m):
            k = len(child_pos[u])
            if k <= 1:
                continue
            cmat = costs[u]
            if k == 2:
                total += cmat[0][1] if cmat[0][1] < cmat[1][0] else cmat[1][0]
                continue
            size = 1 << k
            add = [[0] * size for _ in range(k)]
            for b in range(k):
                ab = add[b]
                for mask in range(1, size):
                    lsb = mask & -mask
                    bit = lsb.bit_length() - 1
                    ab[mask] = ab[mask ^ lsb] + cmat[bit][b]
            dp = [INF] * size
            dp[0] = 0
            for mask in range(size):
                cur = dp[mask]
                if cur == INF:
                    continue
                for b in range(k):
                    if not (mask >> b) & 1:
                        nm = mask | (1 << b)
                        val = cur + add[b][mask]
                        if val < dp[nm]:
                            dp[nm] = val
            total += dp[size - 1]
        return total
