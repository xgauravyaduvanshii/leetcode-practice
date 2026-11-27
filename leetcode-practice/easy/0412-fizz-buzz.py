# LeetCode 412. Fizz Buzz — Easy
# https://leetcode.com/problems/fizz-buzz/
# Submission 2197286276 — Accepted, Python3
#
# My thinking: go from 1 to n and check each number.
# Divisible by both 3 and 5 first — that has to come
# before the single checks, otherwise 15 would just
# say Fizz. Then 3, then 5, otherwise the number itself.

class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        answer = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                answer.append("FizzBuzz")
            elif i % 3 == 0:
                answer.append("Fizz")
            elif i % 5 == 0:
                answer.append("Buzz")
            else:
                answer.append(str(i))
        return answer
