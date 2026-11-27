# LeetCode 2883. Drop Missing Data — Easy
# https://leetcode.com/problems/drop-missing-data/
# Submission 2198686685 — Accepted, Pandas (Python)
#
# My thinking: only the name column decides — a row
# with no name is dropped, while a missing age stays.
# So I drop missing values on the name column alone,
# not on the whole row.

import pandas as pd


def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return students.dropna(subset=["name"])
