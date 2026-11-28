# LeetCode 2512. Reward Top K Students — Medium
# https://leetcode.com/problems/reward-top-k-students/
# Submission 2204978035 — Accepted, Python3
#
# My thinking: score each report at +3 per positive-feedback word
# and -1 per negative-feedback word. Sort by score descending and
# student id ascending, then take the first k ids.
class Solution:
    def topStudents(self, positive_feedback: list[str], negative_feedback: list[str], report: list[str], student_id: list[int], k: int) -> list[int]:
        pos = set(positive_feedback)
        neg = set(negative_feedback)
        scores = []
        for rep, sid in zip(report, student_id):
            score = 0
            for w in rep.split():
                if w in pos:
                    score += 3
                elif w in neg:
                    score -= 1
            scores.append((-score, sid))
        scores.sort()
        return [sid for _, sid in scores[:k]]
