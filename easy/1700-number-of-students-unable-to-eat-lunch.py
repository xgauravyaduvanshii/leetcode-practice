# LeetCode 1700. Number of Students Unable to Eat Lunch — Easy
# https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/
# Submission 2197594176 — Accepted, Python3
#
# My thinking: only the counts of the two sandwich
# types matter, not the queue order — students
# just rotate until someone wants the top sandwich.
# I serve sandwiches in order while a student who
# wants that type is left; when none is left, the
# remaining students are stuck.

class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        counts = [0, 0]
        for s in students:
            counts[s] += 1
        for sandwich in sandwiches:
            if counts[sandwich] == 0:
                break
            counts[sandwich] -= 1
        return counts[0] + counts[1]
