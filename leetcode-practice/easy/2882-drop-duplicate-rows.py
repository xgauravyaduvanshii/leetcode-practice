# LeetCode 2882. Drop Duplicate Rows — Easy
# https://leetcode.com/problems/drop-duplicate-rows/
# Submission 2198686258 — Accepted, Pandas (Python)
#
# My thinking: two rows with the same email are the
# same customer, so I keep only the first row for
# each email and drop the rest.

import pandas as pd


def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.drop_duplicates(subset="email", keep="first")
