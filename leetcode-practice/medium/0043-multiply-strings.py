# LeetCode 43. Multiply Strings — Medium
# https://leetcode.com/problems/multiply-strings/
# Submission 2201083286 — Accepted, Python3
#
# My thinking: I multiply digit by digit the way I would
# on paper, adding each product into its place in the
# answer and carrying the tens along.

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        n1, n2 = len(num1), len(num2)
        result = [0] * (n1 + n2)
        for i in range(n1 - 1, -1, -1):
            for j in range(n2 - 1, -1, -1):
                product = int(num1[i]) * int(num2[j])
                pos = i + j + 1
                total = product + result[pos]
                result[pos] = total % 10
                result[pos - 1] += total // 10
        answer = "".join(str(d) for d in result).lstrip("0")
        return answer or "0"
