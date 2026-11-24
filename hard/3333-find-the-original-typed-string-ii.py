# LeetCode 3333. Find the Original Typed String II — Hard
# https://leetcode.com/problems/find-the-original-typed-string-ii/
# Submission 2202379473 — Accepted, Python3
MOD = 10 ** 9 + 7


class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        # My thinking: split the word into runs of equal letters with
        # lengths c1..cm. The original string chose 1..ci letters from each
        # run, so there are c1 * ... * cm originals in total. I only need
        # to subtract the ones shorter than k: a DP over runs counts, for
        # each length j < k, how many choices sum to exactly j, with prefix
        # sums making each run O(k). If k is at most the number of runs,
        # every original is already long enough and the answer is the total.
        groups = []
        i = 0
        n = len(word)
        while i < n:
            j = i
            while j < n and word[j] == word[i]:
                j += 1
            groups.append(j - i)
            i = j
        m = len(groups)
        total = 1
        for c in groups:
            total = total * c % MOD
        if k <= m:
            return total
        dp = [0] * k
        dp[0] = 1
        for c in groups:
            pref = [0] * (k + 1)
            for j in range(k):
                pref[j + 1] = (pref[j] + dp[j]) % MOD
            ndp = [0] * k
            for j in range(1, k):
                lo = j - c
                if lo < 0:
                    lo = 0
                ndp[j] = (pref[j] - pref[lo]) % MOD
            dp = ndp
        short = sum(dp) % MOD
        return (total - short) % MOD
