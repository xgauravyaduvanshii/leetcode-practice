# LeetCode 2888. Reshape Data: Concatenate — Easy
# https://leetcode.com/problems/reshape-data-concatenate/
# Submission 2198688275 — Accepted, Pandas (Python)
#
# My thinking: the two tables have the same columns,
# so I just stack the second one under the first and
# return the longer table.

import pandas as pd


def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    return pd.concat([df1, df2])
