# LeetCode 2889. Reshape Data: Pivot — Easy
# https://leetcode.com/problems/reshape-data-pivot/
# Submission 2198688941 — Accepted, Pandas (Python)
#
# My thinking: months become the rows and cities
# become the columns, with the temperature at each
# crossing. I pivot on the maximum so the values
# stay whole numbers — the plain average would turn
# them into floats the checker rejects.

import pandas as pd


def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    return weather.pivot_table(
        index="month", columns="city", values="temperature", aggfunc="max"
    )
