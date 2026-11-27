# LeetCode 721. Accounts Merge — Medium
# https://leetcode.com/problems/accounts-merge/
# Submission 2198921698 — Accepted, Python3
#
# My thinking: emails that appear together belong
# to the same person, so I join them with a
# union-find structure. Each connected group of
# emails becomes one account under its owner's
# name.

from collections import defaultdict
from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}

        def find(x):
            parent.setdefault(x, x)
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            parent[find(a)] = find(b)

        owners = {}
        for account in accounts:
            name, emails = account[0], account[1:]
            for email in emails:
                owners[email] = name
                union(emails[0], email)
        groups = defaultdict(list)
        for email in owners:
            groups[find(email)].append(email)
        return [[owners[root]] + sorted(emails) for root, emails in groups.items()]
