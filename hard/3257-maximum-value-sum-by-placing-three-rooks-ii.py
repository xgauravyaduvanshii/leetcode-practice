# LeetCode 3257. Maximum Value Sum by Placing Three Rooks II — Hard
# https://leetcode.com/problems/maximum-value-sum-by-placing-three-rooks-ii/
# Submission 2202152273 — Accepted, Python3
#
# My thinking: this is an assignment problem —
# pick 3 rows and 3 distinct columns to maximise
# the sum. A row's optimal cell must be among its
# top 3, since only two other rooks can block its
# columns. I build a min-cost max-flow network
# (source to rows, rows to their top-3 columns,
# columns to sink) and push 3 units of flow; the
# negated cost is the answer.

from typing import List


class Solution:
    def maximumValueSum(self, board: List[List[int]]) -> int:
        from collections import deque
        m = len(board)
        n = len(board[0])
        N = 2 + m + n
        S = 0
        T = N - 1
        graph = [[] for _ in range(N)]
        def add_edge(fr, to, cap, cost):
            graph[fr].append([to, cap, cost, len(graph[to])])
            graph[to].append([fr, 0, -cost, len(graph[fr]) - 1])
        for i in range(m):
            add_edge(S, 1 + i, 1, 0)
        for j in range(n):
            add_edge(1 + m + j, T, 1, 0)
        for i, row in enumerate(board):
            idx = sorted(range(n), key=lambda j: row[j], reverse=True)[:3]
            for j in idx:
                add_edge(1 + i, 1 + m + j, 1, -row[j])
        INF = 10 ** 18
        res = 0
        flow = 0
        while flow < 3:
            dist = [INF] * N
            inq = [False] * N
            prevv = [-1] * N
            preve = [-1] * N
            dist[S] = 0
            q = deque([S])
            inq[S] = True
            while q:
                v = q.popleft()
                inq[v] = False
                for ei, e in enumerate(graph[v]):
                    if e[1] > 0 and dist[e[0]] > dist[v] + e[2]:
                        dist[e[0]] = dist[v] + e[2]
                        prevv[e[0]] = v
                        preve[e[0]] = ei
                        if not inq[e[0]]:
                            q.append(e[0])
                            inq[e[0]] = True
            if dist[T] == INF:
                break
            v = T
            while v != S:
                e = graph[prevv[v]][preve[v]]
                e[1] -= 1
                graph[v][e[3]][1] += 1
                v = prevv[v]
            res += dist[T]
            flow += 1
        return -res
