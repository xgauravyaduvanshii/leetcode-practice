# LeetCode 3764. Most Common Course Pairs — Hard
# https://leetcode.com/problems/most-common-course-pairs/
# Submission 2203167467 — Accepted, Pandas
import pandas as pd


def topLearnerCourseTransitions(course_completions: pd.DataFrame) -> pd.DataFrame:
    # My thinking: a top performer is a student who finished
    # at least 5 courses with an average rating of 4 or more.
    # For each of them I order their courses by completion
    # date and take each consecutive pair, then count how
    # often each pair occurs. I order by the count
    # descending, then by the two course names ascending
    # case-insensitively, so the order does not depend on
    # how the names were capitalised.
    df = course_completions.copy()
    df["completion_date"] = pd.to_datetime(df["completion_date"])
    stats = df.groupby("user_id").agg(
        course_count=("course_id", "count"),
        avg_rating=("course_rating", "mean"),
    )
    top_users = stats[(stats["course_count"] >= 5) & (stats["avg_rating"] >= 4)].index
    df = df[df["user_id"].isin(top_users)]
    pairs = []
    for _, group in df.groupby("user_id", sort=False):
        ordered = group.sort_values("completion_date", kind="stable")
        names = ordered["course_name"].tolist()
        for first, second in zip(names, names[1:]):
            pairs.append((first, second))
    result = pd.DataFrame(pairs, columns=["first_course", "second_course"])
    if result.empty:
        return pd.DataFrame(columns=["first_course", "second_course", "transition_count"])
    result = (
        result.groupby(["first_course", "second_course"], as_index=False)
        .size()
        .rename(columns={"size": "transition_count"})
    )
    result = result.assign(
        _first_lower=result["first_course"].str.lower(),
        _second_lower=result["second_course"].str.lower(),
    )
    result = result.sort_values(
        ["transition_count", "_first_lower", "_second_lower"],
        ascending=[False, True, True],
    ).drop(columns=["_first_lower", "_second_lower"]).reset_index(drop=True)
    return result
