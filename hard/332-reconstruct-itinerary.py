from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        # My thinking: use every ticket once in lexical order — walk
        # the smallest next airport first (Hierholzer), and record
        # each airport only after its tickets are used up.
        graph = defaultdict(list)
        for src, dst in tickets:
            graph[src].append(dst)
        for src in graph:
            graph[src].sort(reverse=True)
        route = []

        def visit(airport):
            while graph[airport]:
                visit(graph[airport].pop())
            route.append(airport)

        visit("JFK")
        return route[::-1]
