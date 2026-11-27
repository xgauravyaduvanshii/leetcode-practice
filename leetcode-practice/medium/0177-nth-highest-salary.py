# LeetCode 177. Nth Highest Salary — Medium
# https://leetcode.com/problems/nth-highest-salary/
# Submission 2204056503 — Accepted, Pandas
import pandas as pd


def nth_highest_salary(employee: pd.DataFrame, n: int) -> pd.DataFrame:
    # My thinking: distinct salaries sorted highest first
    # put the Nth highest at index N - 1, so drop duplicate
    # salaries, sort them descending, and take that row.
    # If fewer than N distinct salaries exist, there is no
    # Nth highest salary, so return a single NULL row.
    salaries = (
        employee["salary"]
        .drop_duplicates()
        .sort_values(ascending=False)
        .reset_index(drop=True)
    )
    if len(salaries) < n:
        return pd.DataFrame({"getNthHighestSalary(n)": [None]})
    return pd.DataFrame({"getNthHighestSalary(n)": [salaries.iloc[n - 1]]})
