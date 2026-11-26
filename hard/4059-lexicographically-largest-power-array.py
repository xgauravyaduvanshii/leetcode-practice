# LeetCode 4059. Lexicographically Largest Power Array — Hard
# https://leetcode.com/problems/lexicographically-largest-power-array/
# Submission 2203582886 — Accepted, Python3
class Solution:
    def largestPower(self, nums: list[int]) -> list[int]:
        # My thinking: work the bits from high (14) to low
        # (0), since power[0] matters first, then power[1],
        # and so on. Keep the numbers in ordered groups: the
        # groups are the blocks of the permutation fixed by
        # the higher bits, and inside a group the numbers
        # can still be reordered freely without changing any
        # power value already decided. For the current bit,
        # walk the groups in order and put the numbers that
        # have the bit first inside each group, which is the
        # longest leading run of set bits this bit can get.
        # The moment a group has a number without the bit,
        # the run stops there, so split that group into its
        # with-bit part (in the run) and its without-bit part
        # (right after it) — and leave every later group
        # completely alone, because their order no longer
        # affects this bit and splitting them would only
        # steal freedom from the lower bits. A group whose
        # numbers all have the bit just joins the run whole.
        groups = [list(nums)]
        ans = [0] * 15
        for b in range(14, -1, -1):
            new_groups = []
            broken = False
            prefix = 0
            for g in groups:
                if broken:
                    new_groups.append(g)
                    continue
                withb = [x for x in g if (x >> b) & 1]
                without = [x for x in g if not ((x >> b) & 1)]
                if not withb:
                    new_groups.append(g)
                    broken = True
                elif not without:
                    new_groups.append(g)
                    prefix += len(g)
                else:
                    new_groups.append(withb)
                    new_groups.append(without)
                    prefix += len(withb)
                    broken = True
            groups = new_groups
            ans[14 - b] = prefix
        return ans
