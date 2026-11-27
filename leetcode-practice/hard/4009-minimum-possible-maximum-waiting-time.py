# LeetCode 4009. Minimum Possible Maximum Waiting Time — Hard
# https://leetcode.com/problems/minimum-possible-maximum-waiting-time/
# Submission 2203508267 — Accepted, Python3
from typing import List


class Solution:
    def minMaxWaitingTime(self, demand: List[int], fuel: List[int]) -> int:
        # My thinking: cars are served in order, and the
        # process stops at the first car neither dispenser
        # can fuel, so serving k cars means serving cars
        # 0..k-1. Track each dispenser by how much fuel it
        # has left and by its lag — how long until it is
        # free, measured from the start time of the last
        # car served. A lag is at most the biggest demand
        # (20), because a dispenser frees at most one
        # demand after the last car that used it started.
        # When car i takes a dispenser, it waits exactly
        # that dispenser's lag, the clock advances by the
        # lag, the other dispenser's lag shrinks by the
        # same amount (floored at 0), and the chosen
        # dispenser's new lag is demand[i]. The fuel left
        # in dispenser 1 follows from the fuel left in
        # dispenser 0 and the demands served so far, so a
        # state is (fuel0 left, lag0, lag1). Two histories
        # reaching the same state differ only in the worst
        # wait suffered so far, and the smaller one always
        # wins, so keep the minimum worst wait per state.
        # Layer by layer this gives, for the largest
        # reachable number of served cars, the smallest
        # possible maximum waiting time; if not even car 0
        # can be served, the answer is -1.
        n = len(demand)
        total_fuel = fuel[0] + fuel[1]
        inf = 10 ** 9
        cur = {(fuel[0], 0, 0): 0}
        served = 0
        used = 0
        for i in range(n):
            d = demand[i]
            nxt = {}
            for (r0, lag0, lag1), worst in cur.items():
                r1 = total_fuel - used - r0
                if r0 >= d:
                    w = worst if worst > lag0 else lag0
                    key = (r0 - d, d, lag1 - lag0 if lag1 > lag0 else 0)
                    if w < nxt.get(key, inf):
                        nxt[key] = w
                if r1 >= d:
                    w = worst if worst > lag1 else lag1
                    key = (r0, lag0 - lag1 if lag0 > lag1 else 0, d)
                    if w < nxt.get(key, inf):
                        nxt[key] = w
            if not nxt:
                break
            cur = nxt
            served = i + 1
            used += d
        if served == 0:
            return -1
        return min(cur.values())
