class Solution:
    def canSeePersonsCount(self, heights: list[int]) -> list[int]:
        # My thinking: scan from right to left with a decreasing stack of
        # heights. Each person sees every shorter person on the stack until
        # the first taller-or-equal one, which they also see — then that
        # taller person blocks the view of everyone behind them.
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
            answer[i] = count
            stack.append(heights[i])
        return answer
