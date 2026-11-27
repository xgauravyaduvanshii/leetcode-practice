# LeetCode 2877. Create a DataFrame from List — Easy
# https://leetcode.com/problems/create-a-dataframe-from-list/
# Submission 2198427719 — Accepted, Pandas (Python)
#
# My thinking: the list of rows already holds the
# student id and age in order, so I hand it to a
# DataFrame with those two column names and the
# table is done.

import pandas as pd
from typing import List


def createDataFrame(student_data: List[List[int]]) -> pd.DataFrame:
    return pd.DataFrame(student_data, columns=["student_id", "age"])
