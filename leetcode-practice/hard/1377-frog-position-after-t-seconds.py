from collections import deque


class Solution:
    def frogPosition(self, n: int, edges: list[list[int]], t: int, target: int) -> float:
        # My thinking: the frog picks uniformly among the
        # neighbours it has not visited — so walk the tree
        # spreading the probability, and stop the moment the
        # clock runs out or the frog gets stuck.
        graph = [[] for _ in range(n + 1)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        queue = deque([(1, 1.0, 0)])
        seen = {1}
        while queue:
            node, prob, time = queue.popleft()
            if node == target:
                if time == t:
                    return prob
                unvisited = [nb for nb in graph[node] if nb not in seen]
                if not unvisited:
                    return prob
                return 0.0
            if time == t:
                continue
            unvisited = [nb for nb in graph[node] if nb not in seen]
            if not unvisited:
                continue
            for nb in unvisited:
                seen.add(nb)
                queue.append((nb, prob / len(unvisited), time + 1))
        return 0.0
