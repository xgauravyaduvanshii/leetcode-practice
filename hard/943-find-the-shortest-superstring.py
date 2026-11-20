class Solution:
    def shortestSuperstring(self, words: list[str]) -> str:
        # My thinking: the best superstring is a path through the
        # words where each step reuses the biggest overlap — search
        # all orders with a bitmask DP.
        n = len(words)
        overlap = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                for k in range(min(len(words[i]), len(words[j])), 0, -1):
                    if words[i][-k:] == words[j][:k]:
                        overlap[i][j] = k
                        break
        dp = [[-1] * n for _ in range(1 << n)]
        parent = [[-1] * n for _ in range(1 << n)]
        for i in range(n):
            dp[1 << i][i] = 0
        for mask in range(1 << n):
            for last in range(n):
                if dp[mask][last] < 0:
                    continue
                for nxt in range(n):
                    if mask & (1 << nxt):
                        continue
                    new_mask = mask | (1 << nxt)
                    value = dp[mask][last] + overlap[last][nxt]
                    if value > dp[new_mask][nxt]:
                        dp[new_mask][nxt] = value
                        parent[new_mask][nxt] = last
        full = (1 << n) - 1
        last = max(range(n), key=lambda i: dp[full][i])
        order = []
        mask = full
        while last != -1:
            order.append(last)
            prev = parent[mask][last]
            mask ^= 1 << last
            last = prev
        order.reverse()
        result = words[order[0]]
        for i in range(1, len(order)):
            result += words[order[i]][overlap[order[i - 1]][order[i]]:]
        return result
