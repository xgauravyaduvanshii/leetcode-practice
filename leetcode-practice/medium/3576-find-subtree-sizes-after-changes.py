from typing import List


class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        # My thinking: the reparenting is simultaneous, so the "closest
        # same-letter ancestor" of every node is decided on the ORIGINAL
        # tree. A single DFS down the original tree keeps, for each of the
        # 26 letters, a stack of the ancestors carrying that letter on the
        # current root-to-node path - the top of the stack is exactly the
        # closest such ancestor. Each node's new parent is that top element
        # (or its old parent when the stack is empty). Afterwards the new
        # tree is rebuilt from the new parents and subtree sizes are
        # accumulated bottom-up in a reverse BFS order.
        n = len(parent)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)

        new_parent = [-1] * n
        stacks = [[] for _ in range(26)]
        # Iterative DFS with enter/exit markers so the per-letter stacks
        # always mirror the current root-to-node path.
        dfs = [(0, True)]
        while dfs:
            node, entering = dfs.pop()
            c = ord(s[node]) - 97
            if entering:
                new_parent[node] = stacks[c][-1] if stacks[c] else parent[node]
                stacks[c].append(node)
                dfs.append((node, False))
                for ch in reversed(children[node]):
                    dfs.append((ch, True))
            else:
                stacks[c].pop()

        new_children = [[] for _ in range(n)]
        for i in range(1, n):
            new_children[new_parent[i]].append(i)

        sizes = [1] * n
        order = []
        stack = [0]
        while stack:
            u = stack.pop()
            order.append(u)
            for v in new_children[u]:
                stack.append(v)
        for u in reversed(order):
            for v in new_children[u]:
                sizes[u] += sizes[v]
        return sizes
