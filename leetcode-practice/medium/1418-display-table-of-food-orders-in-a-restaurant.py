# LeetCode 1418. Display Table of Food Orders in a Restaurant — Medium
# https://leetcode.com/problems/display-table-of-food-orders-in-a-restaurant/
# Submission 2199055544 — Accepted, Python3
#
# My thinking: I count each food per table,
# then print the table with foods sorted across
# the top and table numbers sorted down the
# side, filling in zeroes where nothing was
# ordered.

from collections import defaultdict
from typing import List


class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        foods = set()
        tables = defaultdict(dict)
        for _, table, food in orders:
            foods.add(food)
            tables[int(table)][food] = tables[int(table)].get(food, 0) + 1
        header = ["Table"] + sorted(foods)
        result = [header]
        for table in sorted(tables):
            result.append([str(table)] + [str(tables[table].get(food, 0)) for food in header[1:]])
        return result
