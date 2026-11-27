# LeetCode 3832. Find Users with Persistent Behavior Patterns — Hard
# https://leetcode.com/problems/find-users-with-persistent-behavior-patterns/
# Submission 2203280009 — Accepted, Pandas
import pandas as pd


def find_behaviorally_stable_users(activity: pd.DataFrame) -> pd.DataFrame:
    # My thinking: a day only counts if the user did exactly
    # one action on it, so first drop every (user, date) with
    # more than one row. On the surviving days a new streak
    # starts whenever the date is not the day after the
    # previous one, or the action changes; a running count
    # of those breaks labels each unbroken same-action run.
    # Each run gives its length and its first and last day;
    # keep runs of at least 5 days, then per user keep the
    # longest one, breaking ties by the lexicographically
    # smallest action and then by the latest start date.
    df = activity.copy()
    df["action_date"] = pd.to_datetime(df["action_date"])
    counts = df.groupby(["user_id", "action_date"]).size()
    single = counts[counts == 1].reset_index()[["user_id", "action_date"]]
    df = df.merge(single, on=["user_id", "action_date"], how="inner")
    df = df.sort_values(["user_id", "action_date"]).reset_index(drop=True)
    df["prev_date"] = df.groupby("user_id")["action_date"].shift(1)
    df["prev_action"] = df.groupby("user_id")["action"].shift(1)
    df["new_run"] = (
        df["prev_date"].isna()
        | (df["action_date"] - df["prev_date"] != pd.Timedelta(days=1))
        | (df["action"] != df["prev_action"])
    )
    df["run_id"] = df.groupby("user_id")["new_run"].cumsum()
    streaks = (
        df.groupby(["user_id", "run_id"])
        .agg(
            action=("action", "first"),
            streak_length=("action_date", "size"),
            start_date=("action_date", "min"),
            end_date=("action_date", "max"),
        )
        .reset_index()
    )
    streaks = streaks[streaks["streak_length"] >= 5]
    if streaks.empty:
        return pd.DataFrame(
            columns=["user_id", "action", "streak_length", "start_date", "end_date"]
        )
    streaks = streaks.sort_values(
        ["user_id", "streak_length", "action", "start_date"],
        ascending=[True, False, True, False],
    )
    best = streaks.drop_duplicates(subset=["user_id"], keep="first")
    best = best.sort_values(["streak_length", "user_id"], ascending=[False, True])
    return best[
        ["user_id", "action", "streak_length", "start_date", "end_date"]
    ].reset_index(drop=True)
