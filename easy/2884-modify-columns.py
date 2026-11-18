# LeetCode 2884. Modify Columns — Easy
# https://leetcode.com/problems/modify-columns/
# Submission 2198686960 — Accepted, Pandas (Python)
#
# My thinking: every salary doubles in place — I
# multiply the salary column by two and return the
# same table.

import pandas as pd


def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees["salary"] = employees["salary"] * 2
    return employees
