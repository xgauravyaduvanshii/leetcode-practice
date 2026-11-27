# LeetCode 2890. Reshape Data: Melt — Easy
# https://leetcode.com/problems/reshape-data-melt/
# Submission 2198692760 — Accepted, Pandas (Python)
#
# My thinking: the quarters are spread across four
# columns and need to become rows instead. Melting
# on the product column turns each quarter column
# into a quarter-and-sales pair underneath it.

import pandas as pd


def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    return report.melt(id_vars=["product"], var_name="quarter", value_name="sales")
