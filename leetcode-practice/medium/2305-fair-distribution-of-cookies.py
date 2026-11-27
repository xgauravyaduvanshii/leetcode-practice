# LeetCode 2305. Fair Distribution of Cookies — Medium
# https://leetcode.com/problems/fair-distribution-of-cookies/
# Submission 2204664099 — Accepted, Python3
#
# My thinking: try every way to hand the cookie bags to the k children
# with a depth-first search, biggest bags first. Two prunings keep it
# fast: skip a child whose current load equals one already tried (the
# children are interchangeable), and stop a branch as soon as its
# biggest load reaches the best answer found so far. The best unfairness
# seen is the answer.
class Solution:
    def distributeCookies(self, cookies: list[int], k: int) -> int:
        cookies.sort(reverse=True)
        n = len(cookies)
        loads = [0] * k
        best = sum(cookies)

        def dfs(i):
            nonlocal best
            if i == n:
                best = min(best, max(loads))
                return
            seen = set()
            for j in range(k):
                if loads[j] in seen:
                    continue
                seen.add(loads[j])
                loads[j] += cookies[i]
                if max(loads) < best:
                    dfs(i + 1)
                loads[j] -= cookies[i]
                if loads[j] == 0:
                    break

        dfs(0)
        return best
