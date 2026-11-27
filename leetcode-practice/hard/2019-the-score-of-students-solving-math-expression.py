# LeetCode 2019. The Score of Students Solving Math Expression — Hard
# https://leetcode.com/problems/the-score-of-students-solving-math-expression/
# Submission 2201316118 — Accepted, Python3
#
# My thinking: the right answer earns 5, any other
# answer a wrong order of operations could still
# produce earns 2 — so I work out the right
# answer first, then every value any bracketing
# can reach, capped at 1000.

class Solution:
    def scoreOfStudents(self, s: str, answers: list[int]) -> int:
        nums = []
        ops = []
        i = 0
        while i < len(s):
            if s[i].isdigit():
                j = i
                while j < len(s) and s[j].isdigit():
                    j += 1
                nums.append(int(s[i:j]))
                i = j
            else:
                ops.append(s[i])
                i += 1
        # Correct answer: multiplication before addition.
        terms = []
        cur = nums[0]
        for k in range(len(ops)):
            if ops[k] == '*':
                cur = cur * nums[k + 1]
            else:
                terms.append(cur)
                cur = nums[k + 1]
        terms.append(cur)
        correct = sum(terms)
        # Every value any bracketing can reach, capped at 1000.
        n = len(nums)
        dp = [[set() for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i].add(nums[i])
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                for k in range(i, j):
                    for a in dp[i][k]:
                        for b in dp[k + 1][j]:
                            v = a + b if ops[k] == '+' else a * b
                            if v <= 1000:
                                dp[i][j].add(v)
        achievable = dp[0][n - 1]
        total = 0
        for a in answers:
            if a == correct:
                total += 5
            elif a in achievable:
                total += 2
        return total
