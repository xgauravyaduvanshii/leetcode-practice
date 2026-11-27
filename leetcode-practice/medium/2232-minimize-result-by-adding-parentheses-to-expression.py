# LeetCode 2232. Minimize Result by Adding Parentheses to Expression — Medium
# https://leetcode.com/problems/minimize-result-by-adding-parentheses-to-expression/
# Submission 2204511164 — Accepted, Python3
#
# My thinking: the parentheses must wrap the '+' with one split on each
# side, so there are only a few placements to try. For each placement
# the value is left * (mid_left + mid_right) * right, where a missing
# outer part counts as 1. I evaluate every placement and keep the
# expression string with the smallest value.
class Solution:
    def minimizeResult(self, expression: str) -> str:
        plus = expression.index('+')
        n = len(expression)
        best_val = float('inf')
        best = expression
        for i in range(plus):
            left = int(expression[:i]) if i > 0 else 1
            mid_left = int(expression[i:plus])
            for j in range(plus + 2, n + 1):
                mid_right = int(expression[plus + 1:j])
                right = int(expression[j:]) if j < n else 1
                val = left * (mid_left + mid_right) * right
                if val < best_val:
                    best_val = val
                    best = expression[:i] + '(' + expression[i:j] + ')' + expression[j:]
        return best
