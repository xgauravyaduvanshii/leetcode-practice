from collections import defaultdict


class Solution:
    def minEdgeReversals(self, n: int, edges: list[list[int]]) -> list[int]:
        # My thinking: first count how many edges point away from node 0
        # (that is the answer for 0). Moving the root across an edge flips
        # the count by exactly one: +1 if the edge pointed toward the old
        # root, -1 if it pointed away.
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append((v, 0))  # going u -> v needs no reversal
            graph[v].append((u, 1))  # going v -> u needs one reversal
        answer = [0] * n
        # count reversals needed with 0 as the root
        stack = [0]
        seen = {0}
        while stack:
            node = stack.pop()
            for nxt, cost in graph[node]:
                if nxt not in seen:
                    seen.add(nxt)
                    answer[0] += cost
                    stack.append(nxt)
        # re-root: moving the root across an edge changes the count by +-1
        def dfs(node: int, parent: int) -> None:
            for nxt, cost in graph[node]:
                if nxt == parent:
                    continue
                answer[nxt] = answer[node] + (1 if cost == 0 else -1)
                dfs(nxt, node)

        dfs(0, -1)
        return answer
