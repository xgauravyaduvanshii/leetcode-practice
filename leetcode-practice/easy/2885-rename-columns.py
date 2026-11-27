# LeetCode 2885. Rename Columns — Easy
# https://leetcode.com/problems/rename-columns/
# Submission 2198687268 — Accepted, Pandas (Python)
#
# My thinking: the columns just need their new names
# — id becomes student_id, first and last become
# first_name and last_name, and age becomes
# age_in_years. A rename with that mapping does it.

import pandas as pd


def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    return students.rename(
        columns={
            "id": "student_id",
            "first": "first_name",
            "last": "last_name",
            "age": "age_in_years",
        }
    )
