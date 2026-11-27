class Solution:
    def minimumDistance(self, word: str) -> int:
        # My thinking: one finger always sits on the last letter
        # typed, so only the other finger's position matters —
        # keep the cheapest cost for each spot it could be.
        def dist(a, b):
            if a == 27 or b == 27:
                return 0
            ar, ac = divmod(a, 6)
            br, bc = divmod(b, 6)
            return abs(ar - br) + abs(ac - bc)

        n = len(word)
        INF = float("inf")
        dp = [INF] * 28
        dp[27] = 0
        for i in range(1, n):
            cur = [INF] * 28
            prev_char = ord(word[i - 1]) - ord("A")
            char = ord(word[i]) - ord("A")
            for other in range(28):
                if dp[other] == INF:
                    continue
                cur[other] = min(cur[other], dp[other] + dist(prev_char, char))
                cur[prev_char] = min(cur[prev_char], dp[other] + dist(other, char))
            dp = cur
        return min(dp)
