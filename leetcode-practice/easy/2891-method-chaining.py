# LeetCode 2891. Method Chaining — Easy
# https://leetcode.com/problems/method-chaining/
# Submission 2198693139 — Accepted, Pandas (Python)
#
# My thinking: heavy animals are the ones over 100,
# heaviest first, and only the name matters. One
# chain does it — filter, sort descending by weight,
# then keep the name column.

import pandas as pd


def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    return animals[animals["weight"] > 100].sort_values(
        "weight", ascending=False
    )[["name"]]
