# LeetCode 1944. Number of Visible People in a Queue — Hard
# https://leetcode.com/problems/number-of-visible-people-in-a-queue/
# Submission 2200858831 — Accepted, Python3
#
# My thinking: scan from right to left with a strictly decreasing stack of
# heights. Each person sees every shorter person on the stack until the
# first taller-or-equal one, which they also see — then that taller person
# blocks the view of everyone behind them. An equal-height person is seen
# but then leaves the stack, because the nearer equal height hides it
# from everyone further left.

class Solution:
    def canSeePersonsCount(self, heights: list[int]) -> list[int]:
        n = len(heights)
        answer = [0] * n
        stack = []
        for i in range(n - 1, -1, -1):
            count = 0
            while stack and heights[i] > stack[-1]:
                stack.pop()
                count += 1
            if stack:
                count += 1
                if stack[-1] == heights[i]:
                    stack.pop()
            answer[i] = count
            stack.append(heights[i])
        return answer
