class Solution:
    def criticalConnections(self, n: int, connections: list[list[int]]) -> list[list[int]]:
        # My thinking: a link is critical when no back edge
        # reaches past it — Tarjan's discovery times find those,
        # done iteratively so deep graphs never blow the stack.
        graph = [[] for _ in range(n)]
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
        disc = [-1] * n
        low = [0] * n
        time = 0
        bridges = []
        for start in range(n):
            if disc[start] != -1:
                continue
            disc[start] = low[start] = time
            time += 1
            stack = [(start, -1, 0)]
            while stack:
                node, parent, idx = stack[-1]
                if idx < len(graph[node]):
                    stack[-1] = (node, parent, idx + 1)
                    nxt = graph[node][idx]
                    if nxt == parent:
                        continue
                    if disc[nxt] == -1:
                        disc[nxt] = low[nxt] = time
                        time += 1
                        stack.append((nxt, node, 0))
                    else:
                        low[node] = min(low[node], disc[nxt])
                else:
                    stack.pop()
                    if parent != -1:
                        low[parent] = min(low[parent], low[node])
                        if low[node] > disc[parent]:
                            bridges.append([parent, node])
        return bridges
