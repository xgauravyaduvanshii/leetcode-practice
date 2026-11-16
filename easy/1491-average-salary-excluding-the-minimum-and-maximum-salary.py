# LeetCode 1491. Average Salary Excluding the Minimum and Maximum Salary — Easy
# https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/
# Submission 2197582154 — Accepted, Python3
#
# My thinking: I add up all the salaries, take away
# the smallest and the largest, and divide by how
# many are left. That is the average of the rest.

class Solution:
    def average(self, salary: list[int]) -> float:
        return (sum(salary) - min(salary) - max(salary)) / (len(salary) - 2)
