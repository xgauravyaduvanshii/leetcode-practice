# LeetCode 2880. Select Data — Easy
# https://leetcode.com/problems/select-data/
# Submission 2198685603 — Accepted, Pandas (Python)
#
# My thinking: I only need the one row whose student
# id is 101, and from it just the name and the age —
# a filter on the id, then the two columns.

import pandas as pd


def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students.loc[students["student_id"] == 101, ["name", "age"]]
