# LeetCode 3482. Analyze Organization Hierarchy — Hard
# https://leetcode.com/problems/analyze-organization-hierarchy/
# Submission 2202672931 — Accepted 11/11, Pandas
#
# My thinking: I walk down from the CEO to give every employee a level,
# keeping the visit order so that parents always come before their reports.
# Walking that order backwards then adds each person's subtree up into
# their manager: the team size is the subtree size minus the person
# themselves, and the budget is the subtree's salaries summed together.
# The answer is sorted by level, then by budget from large to small, then
# by name.

import pandas as pd


def analyze_organization(employees: pd.DataFrame) -> pd.DataFrame:
    children = {}
    info = {}
    ceo = None
    for _, row in employees.iterrows():
        eid = int(row["employee_id"])
        info[eid] = (row["employee_name"], int(row["salary"]))
        mid = row["manager_id"]
        if pd.isna(mid):
            ceo = eid
        else:
            children.setdefault(int(mid), []).append(eid)
    level = {ceo: 1}
    order = [ceo]
    stack = [ceo]
    while stack:
        u = stack.pop()
        for v in children.get(u, []):
            level[v] = level[u] + 1
            order.append(v)
            stack.append(v)
    size = {eid: 1 for eid in info}
    budget = {eid: info[eid][1] for eid in info}
    for u in reversed(order):
        for v in children.get(u, []):
            size[u] += size[v]
            budget[u] += budget[v]
    rows = [
        {
            "employee_id": eid,
            "employee_name": name,
            "level": level[eid],
            "team_size": size[eid] - 1,
            "budget": budget[eid],
        }
        for eid, (name, _sal) in info.items()
    ]
    df = pd.DataFrame(rows)
    df = df.sort_values(
        by=["level", "budget", "employee_name"], ascending=[True, False, True]
    )
    return df[["employee_id", "employee_name", "level", "team_size", "budget"]]
