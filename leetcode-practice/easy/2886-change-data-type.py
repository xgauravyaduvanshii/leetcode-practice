# LeetCode 2886. Change Data Type — Easy
# https://leetcode.com/problems/change-data-type/
# Submission 2198687631 — Accepted, Pandas (Python)
#
# My thinking: the grade column holds whole numbers
# stored as floats, so I cast it to int and return
# the table.

import pandas as pd


def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students["grade"] = students["grade"].astype(int)
    return students
