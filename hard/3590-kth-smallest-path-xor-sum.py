# LeetCode 3590. Kth Smallest Path XOR Sum — Hard
# https://leetcode.com/problems/kth-smallest-path-xor-sum/
# Submission 2202863989 — Accepted, Python3
import sys
import bisect
from typing import List
from collections import defaultdict


class Solution:
    def kthSmallest(self, par: List[int], vals: List[int], queries: List[List[int]]) -> List[int]:
        # My thinking: the path XOR to a node is the XOR of the
        # values on the root path, so each subtree just needs the
        # sorted list of the distinct path XORs inside it. I build
        # those lists bottom-up, always merging the smaller list
        # into the larger one, and answer each query by indexing
        # straight into its node's sorted list.
        sys.setrecursionlimit(100000)
        n = len(vals)
        children = defaultdict(list)
        for i in range(1, n):
            children[par[i]].append(i)
        pref = [0] * n
        pref[0] = vals[0]
        order = [0]
        for u in order:
            for v in children[u]:
                pref[v] = pref[u] ^ vals[v]
                order.append(v)
        q_by_node = defaultdict(list)
        for qi, (u, k) in enumerate(queries):
            q_by_node[u].append((qi, k))
        ans = [-1] * len(queries)

        def dfs(u):
            best = None
            for v in children[u]:
                lst = dfs(v)
                if best is None:
                    best = lst
                    continue
                if len(lst) > len(best):
                    best, lst = lst, best
                merged = []
                i = j = 0
                while i < len(best) and j < len(lst):
                    if best[i] < lst[j]:
                        merged.append(best[i])
                        i += 1
                    elif best[i] > lst[j]:
                        merged.append(lst[j])
                        j += 1
                    else:
                        merged.append(best[i])
                        i += 1
                        j += 1
                merged.extend(best[i:])
                merged.extend(lst[j:])
                best = merged
            if best is None:
                best = []
            idx = bisect.bisect_left(best, pref[u])
            if idx == len(best) or best[idx] != pref[u]:
                best.insert(idx, pref[u])
            for qi, k in q_by_node[u]:
                if k <= len(best):
                    ans[qi] = best[k - 1]
            return best

        dfs(0)
        return ans
