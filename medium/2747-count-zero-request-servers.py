# LeetCode 2747. Count Zero Request Servers — Medium
# https://leetcode.com/problems/count-zero-request-servers/
# Submission 2205239211 — Accepted, Python3
#
# My thinking: sort the logs by time and answer the queries
# in increasing time order with a sliding window [q-x, q]:
# extend the right end with every log at or before q, drop
# logs older than q-x from the left, and count how many
# servers have at least one log still in the window. The
# answer for a query is n minus that count.
class Solution:
    def countServers(self, n: int, logs: list[list[int]], x: int, queries: list[int]) -> list[int]:
        logs.sort(key=lambda log: log[1])
        order = sorted(range(len(queries)), key=lambda i: queries[i])
        cnt = [0] * (n + 1)
        active = 0
        ans = [0] * len(queries)
        left = right = 0
        for qi in order:
            q = queries[qi]
            while right < len(logs) and logs[right][1] <= q:
                server = logs[right][0]
                if cnt[server] == 0:
                    active += 1
                cnt[server] += 1
                right += 1
            while left < right and logs[left][1] < q - x:
                server = logs[left][0]
                cnt[server] -= 1
                if cnt[server] == 0:
                    active -= 1
                left += 1
            ans[qi] = n - active
        return ans
