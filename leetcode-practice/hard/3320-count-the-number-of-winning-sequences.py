# LeetCode 3320. Count The Number of Winning Sequences — Hard
# https://leetcode.com/problems/count-the-number-of-winning-sequences/
# Submission 2202366843 — Accepted, Python3
from typing import List

MOD = 10 ** 9 + 7


class Solution:
    def countWinningSequences(self, s: str) -> int:
        # My thinking: Bob's move in each round is F, W or E, never the same
        # twice in a row, and Alice's move is fixed. I track the score
        # difference (Bob's points minus Alice's) with a DP over rounds,
        # keyed by Bob's last move and the running difference, which ranges
        # from -n to n. A move gains +1 if it beats Alice's creature, -1 if
        # Alice's beats it, 0 on a tie (F beats E, W beats F, E beats W).
        # The answer is the number of sequences ending with a difference > 0.
        beats = {0: 2, 1: 0, 2: 1}  # 0 = F, 1 = W, 2 = E
        code = {'F': 0, 'W': 1, 'E': 2}
        n = len(s)
        alice = [code[c] for c in s]

        def gain(b: int, a: int) -> int:
            if beats[b] == a:
                return 1
            if beats[a] == b:
                return -1
            return 0

        width = 2 * n + 1
        dp = [[0] * width for _ in range(3)]
        for b in range(3):
            dp[b][gain(b, alice[0]) + n] = 1
        for i in range(1, n):
            ndp = [[0] * width for _ in range(3)]
            for last in range(3):
                row = dp[last]
                for d in range(width):
                    v = row[d]
                    if not v:
                        continue
                    for b in range(3):
                        if b == last:
                            continue
                        nd = d + gain(b, alice[i])
                        ndp[b][nd] = (ndp[b][nd] + v) % MOD
            dp = ndp
        ans = 0
        for last in range(3):
            for d in range(n + 1, width):
                ans = (ans + dp[last][d]) % MOD
        return ans
