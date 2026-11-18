# LeetCode 2887. Fill Missing Data — Easy
# https://leetcode.com/problems/fill-missing-data/
# Submission 2198687983 — Accepted, Pandas (Python)
#
# My thinking: a missing quantity just means zero
# stock, so I fill the empty cells in the quantity
# column with 0 and leave everything else alone.

import pandas as pd


def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products["quantity"] = products["quantity"].fillna(0)
    return products
