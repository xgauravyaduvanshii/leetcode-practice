# LeetCode 2037. Minimum Number of Moves to Seat Everyone — Easy
# https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/
# Submission 2197610052 — Accepted, Python3
#
# My thinking: I sort both the seats and the
# students. Matching them in order — smallest seat
# to smallest student, and so on — gives the
# smallest total distance, which is the sum of the
# absolute differences.

class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        seats.sort()
        students.sort()
        return sum(abs(a - b) for a, b in zip(seats, students))
