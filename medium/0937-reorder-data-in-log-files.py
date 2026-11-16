# LeetCode 937. Reorder Data in Log Files — Medium
# https://leetcode.com/problems/reorder-data-in-log-files/
# Submission 2197543806 — Accepted, Python3
#
# My thinking: I split the logs into letter-logs and
# digit-logs. Letter-logs get sorted by their
# content first, then by their identifier if the
# content ties. Digit-logs keep their original
# order and go after all the letter-logs.

class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        letter_logs = []
        digit_logs = []
        for log in logs:
            identifier, rest = log.split(" ", 1)
            if rest[0].isalpha():
                letter_logs.append((rest, identifier, log))
            else:
                digit_logs.append(log)
        letter_logs.sort(key=lambda x: (x[0], x[1]))
        return [log for _, _, log in letter_logs] + digit_logs
