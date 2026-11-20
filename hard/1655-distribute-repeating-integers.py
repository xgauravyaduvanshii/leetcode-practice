from collections import Counter


class Solution:
    def canDistribute(self, nums: list[int], quantity: list[int]) -> bool:
        # My thinking: the hungriest customer picks first —
        # give them any value with enough copies left, and
        # remember the dead ends so they are not retried.
        counts = sorted(Counter(nums).values(), reverse=True)
        quantity = sorted(quantity, reverse=True)
        memo = {}

        def dfs(qi, state):
            if qi == len(quantity):
                return True
            key = (qi, state)
            if key in memo:
                return memo[key]
            q = quantity[qi]
            seen = set()
            for i, c in enumerate(state):
                if c < q or c in seen:
                    continue
                seen.add(c)
                new_state = list(state)
                new_state[i] -= q
                new_state.sort(reverse=True)
                if dfs(qi + 1, tuple(new_state)):
                    memo[key] = True
                    return True
            memo[key] = False
            return False

        return dfs(0, tuple(counts))
