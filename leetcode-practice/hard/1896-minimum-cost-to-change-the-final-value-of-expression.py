# LeetCode 1896. Minimum Cost to Change the Final Value of Expression — Hard
# https://leetcode.com/problems/minimum-cost-to-change-the-final-value-of-expression/
# Submission 2201221257 — Accepted, Python3
#
# My thinking: every subexpression carries its
# value and the cheapest price to flip it — a
# digit costs one to flip, and for an operator I
# either flip a child or flip the operator itself
# and one child, whichever is cheaper.

class Solution:
    def minOperationsToFlip(self, expression: str) -> int:
        s = expression
        i = 0

        def parse_term():
            nonlocal i
            if s[i] == '(':
                i += 1
                val = parse_expr()
                i += 1
                return val
            v = int(s[i])
            i += 1
            return (v, 1)

        def combine(l, r, op):
            lv, lc = l
            rv, rc = r
            if op == '&':
                val = lv & rv
                if lv == 1 and rv == 1:
                    cost = min(lc, rc)
                elif lv == 0 and rv == 0:
                    cost = min(lc + rc, min(lc, rc) + 1)
                elif lv == 0:
                    cost = min(lc, 1)
                else:
                    cost = min(rc, 1)
            else:
                val = lv | rv
                if lv == 0 and rv == 0:
                    cost = min(lc, rc)
                elif lv == 1 and rv == 1:
                    cost = min(lc + rc, min(lc, rc) + 1)
                elif lv == 1:
                    cost = min(lc, 1)
                else:
                    cost = min(rc, 1)
            return (val, cost)

        def parse_expr():
            nonlocal i
            left = parse_term()
            while i < len(s) and s[i] in '&|':
                op = s[i]
                i += 1
                right = parse_term()
                left = combine(left, right, op)
            return left

        val, cost = parse_expr()
        return cost
