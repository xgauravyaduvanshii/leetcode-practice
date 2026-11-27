# LeetCode 2881. Create a New Column — Easy
# https://leetcode.com/problems/create-a-new-column/
# Submission 2198685908 — Accepted, Pandas (Python)
#
# My thinking: the bonus is just twice the salary, so
# I add a new column with that value for every row
# and hand the table back.

import pandas as pd


def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees["bonus"] = employees["salary"] * 2
    return employees
