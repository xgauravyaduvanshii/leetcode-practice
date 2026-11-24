# LeetCode 3617. Find Students with Study Spiral Pattern — Hard
# https://leetcode.com/problems/find-students-with-study-spiral-pattern/
# Submission 2202876876 — Accepted, Pandas
import pandas as pd
from datetime import timedelta


def find_spiral_students(students: pd.DataFrame, study_sessions: pd.DataFrame) -> pd.DataFrame:
    # My thinking: for each student I read the sessions in date
    # order. The cycle length is fixed by the first subject: it is
    # the distance to its next appearance. A student qualifies
    # when that length is at least 3, the sessions run for at
    # least two full cycles, the subjects repeat with that period,
    # the subjects in one cycle are all different, and no two
    # consecutive sessions are more than 2 days apart. The total
    # hours are the sum over the student's sessions, ordered by
    # cycle length then hours, both descending.
    sessions = study_sessions.sort_values(["student_id", "session_date", "session_id"]).copy()
    sessions["session_date"] = pd.to_datetime(sessions["session_date"])
    rows = []
    for student_id, group in sessions.groupby("student_id", sort=False):
        group = group.reset_index(drop=True)
        subjects = group["subject"].tolist()
        dates = group["session_date"].tolist()
        n = len(subjects)
        if n < 6:
            continue
        first = subjects[0]
        second_pos = None
        for i in range(1, n):
            if subjects[i] == first:
                second_pos = i
                break
        if second_pos is None:
            continue
        L = second_pos
        if L < 3 or n < 2 * L:
            continue
        if len(set(subjects[:L])) != L:
            continue
        if any(subjects[i] != subjects[i - L] for i in range(L, n)):
            continue
        if any((dates[i] - dates[i - 1]) > timedelta(days=2) for i in range(1, n)):
            continue
        info = students[students["student_id"] == student_id]
        if info.empty:
            continue
        rows.append({
            "student_id": student_id,
            "student_name": info.iloc[0]["student_name"],
            "major": info.iloc[0]["major"],
            "cycle_length": L,
            "total_study_hours": float(group["hours_studied"].sum()),
        })
    result = pd.DataFrame(rows, columns=["student_id", "student_name", "major", "cycle_length", "total_study_hours"])
    if result.empty:
        return result
    return result.sort_values(["cycle_length", "total_study_hours"], ascending=[False, False]).reset_index(drop=True)
