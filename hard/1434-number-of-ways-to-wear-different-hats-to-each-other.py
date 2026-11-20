class Solution:
    def numberWays(self, hats: list[list[int]]) -> int:
        # My thinking: give the hats out one by one — each hat
        # can go to any person who likes it and has none yet —
        # and a bitmask remembers who is already wearing one.
        MOD = 10 ** 9 + 7
        n = len(hats)
        likes = [[] for _ in range(41)]
        for person, wanted in enumerate(hats):
            for h in wanted:
                likes[h].append(person)
        dp = [0] * (1 << n)
        dp[0] = 1
        for h in range(1, 41):
            for mask in range((1 << n) - 1, -1, -1):
                for person in likes[h]:
                    if not mask & (1 << person):
                        dp[mask | (1 << person)] = (dp[mask | (1 << person)] + dp[mask]) % MOD
        return dp[(1 << n) - 1]
