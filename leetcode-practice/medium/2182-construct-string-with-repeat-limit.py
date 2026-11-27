# LeetCode 2182. Construct String With Repeat Limit — Medium
# https://leetcode.com/problems/construct-string-with-repeat-limit/
# Submission 2204490659 — Accepted, Python3
#
# My thinking: to make the lexicographically largest string I always
# take as many as allowed of the biggest remaining letter, up to the
# repeat limit. If that letter still has copies left, I must insert one
# copy of the next biggest available letter as a breaker before I can
# use it again; if no smaller letter exists, the string is finished.
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        from collections import Counter
        cnt = Counter(s)
        res = []
        while True:
            largest = -1
            for i in range(25, -1, -1):
                if cnt[chr(97 + i)] > 0:
                    largest = i
                    break
            if largest == -1:
                break
            ch = chr(97 + largest)
            use = min(cnt[ch], repeatLimit)
            res.append(ch * use)
            cnt[ch] -= use
            if cnt[ch] > 0:
                breaker = -1
                for i in range(largest - 1, -1, -1):
                    if cnt[chr(97 + i)] > 0:
                        breaker = i
                        break
                if breaker == -1:
                    break
                bch = chr(97 + breaker)
                res.append(bch)
                cnt[bch] -= 1
        return ''.join(res)
