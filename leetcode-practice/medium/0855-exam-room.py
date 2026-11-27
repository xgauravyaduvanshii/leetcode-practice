# LeetCode 855. Exam Room — Medium
# https://leetcode.com/problems/exam-room/
# Submission 2198956126 — Accepted, Python3
#
# My thinking: the best empty seat is the middle
# of the widest gap between taken seats, or an
# end when the edge stretch is longer. I keep the
# taken seats sorted and check every gap.

class ExamRoom:
    def __init__(self, n: int):
        self.n = n
        self.taken = []

    def seat(self) -> int:
        if not self.taken:
            seat = 0
        else:
            best = self.taken[0]
            best_dist = self.taken[0]
            for i in range(len(self.taken) - 1):
                left, right = self.taken[i], self.taken[i + 1]
                middle = (left + right) // 2
                if (right - left) // 2 > best_dist:
                    best_dist = (right - left) // 2
                    best = middle
            if self.n - 1 - self.taken[-1] > best_dist:
                best = self.n - 1
            seat = best
        self.taken.append(seat)
        self.taken.sort()
        return seat

    def leave(self, p: int) -> None:
        self.taken.remove(p)
