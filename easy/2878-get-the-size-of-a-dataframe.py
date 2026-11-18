# LeetCode 2878. Get the Size of a DataFrame — Easy
# https://leetcode.com/problems/get-the-size-of-a-dataframe/
# Submission 2198428683 — Accepted, Pandas (Python)
#
# My thinking: the size of a table is just its row
# count and its column count, which the DataFrame
# already knows — I return them as a two-item list.

import pandas as pd
from typing import List


def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return [players.shape[0], players.shape[1]]
