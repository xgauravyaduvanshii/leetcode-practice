from collections import defaultdict, deque


class Solution:
    def sortItems(self, n: int, m: int, group: list[int], beforeItems: list[list[int]]) -> list[int]:
        # My thinking: sort the groups first, then the items
        # inside each group — two topological sorts, one nested
        # in the other, with ungrouped items in groups of one.
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1
        group_graph = defaultdict(list)
        group_indegree = {g: 0 for g in range(m)}
        for i in range(n):
            for before in beforeItems[i]:
                if group[before] != group[i]:
                    group_graph[group[before]].append(group[i])
                    group_indegree[group[i]] += 1

        def topo_sort(graph, indegree):
            queue = deque([x for x, d in indegree.items() if d == 0])
            order = []
            while queue:
                node = queue.popleft()
                order.append(node)
                for nxt in graph.get(node, []):
                    indegree[nxt] -= 1
                    if indegree[nxt] == 0:
                        queue.append(nxt)
            return order if len(order) == len(indegree) else []

        group_order = topo_sort(group_graph, group_indegree)
        if not group_order:
            return []
        items_by_group = defaultdict(list)
        for i in range(n):
            items_by_group[group[i]].append(i)
        result = []
        for g in group_order:
            members = items_by_group[g]
            sub_graph = defaultdict(list)
            sub_indegree = {i: 0 for i in members}
            for i in members:
                for before in beforeItems[i]:
                    if group[before] == g:
                        sub_graph[before].append(i)
                        sub_indegree[i] += 1
            order = topo_sort(sub_graph, sub_indegree)
            if not order:
                return []
            result.extend(order)
        return result
