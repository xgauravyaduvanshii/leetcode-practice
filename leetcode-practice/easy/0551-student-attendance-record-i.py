# LeetCode 551. Student Attendance Record I — Easy
# https://leetcode.com/problems/student-attendance-record-i/
# Submission 2197496024 — Accepted, Python3
#
# My thinking: a student is rewarded unless they
# were absent twice or more, or late three days in
# a row. So I just count the A's and check whether
# "LLL" appears anywhere in the record.

class Solution:
    def checkRecord(self, s: str) -> bool:
        return s.count("A") < 2 and "LLL" not in s
