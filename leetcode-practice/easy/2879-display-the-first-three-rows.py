# LeetCode 2879. Display the First Three Rows — Easy
# https://leetcode.com/problems/display-the-first-three-rows/
# Submission 2198429585 — Accepted, Pandas (Python)
#
# My thinking: the first three rows are exactly what
# head(3) returns — the rest of the table is simply
# left out.

import pandas as pd


def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)
