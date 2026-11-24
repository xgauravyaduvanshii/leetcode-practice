# LeetCode 3389. Minimum Operations to Make Character Frequencies Equal — Hard
# https://leetcode.com/problems/minimum-operations-to-make-character-frequencies-equal/
# Submission 2202499677 — Accepted 773/773, Python3


class Solution:
    def makeStringGood(self, s: str) -> int:
        # My thinking: pick the target frequency every kept letter ends
        # up with, then walk the alphabet left to right. Letters only ever
        # change forward, so surplus characters are carried to the next
        # letter at one operation a step, which beats deleting one here
        # and inserting one there (two operations). At each letter I either
        # keep it at the target, paying to drop the surplus or fill the
        # shortfall, or drop it to zero, paying for all its characters;
        # either way the carried surplus can be anything up to the target,
        # so I keep the cheapest cost per carry and take a suffix minimum
        # over it. The last letter cannot carry anything past 'z'.
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - 97] += 1
        best = len(s)
        for target in range(1, max(cnt) + 1):
            dp = [float("inf")] * (target + 1)
            dp[0] = 0
            for i in range(26):
                c = cnt[i]
                last = i == 25
                best_at = [float("inf")] * (target + 2)
                for carry in range(target + 1):
                    if dp[carry] == float("inf"):
                        continue
                    avail = c + carry
                    if avail >= target:
                        v = dp[carry] + avail - target
                        u = 0 if last else min(avail - target, target)
                        if v < best_at[u]:
                            best_at[u] = v
                    else:
                        v = dp[carry] + target - avail
                        if v < best_at[0]:
                            best_at[0] = v
                    v = dp[carry] + avail
                    u = 0 if last else min(avail, target)
                    if v < best_at[u]:
                        best_at[u] = v
                ndp = [float("inf")] * (target + 1)
                suf = float("inf")
                for j in range(target, -1, -1):
                    if best_at[j] < suf:
                        suf = best_at[j]
                    ndp[j] = suf
                dp = ndp
            best = min(best, dp[0])
        return best
