# LeetCode 3673. Find Zombie Sessions — Hard
# https://leetcode.com/problems/find-zombie-sessions/
# Submission 2203033181 — Accepted, Pandas
import pandas as pd


def find_zombie_sessions(app_events: pd.DataFrame) -> pd.DataFrame:
    # My thinking: I group the events by session (and user),
    # then measure each session: whole minutes from its first
    # to its last event, how many scrolls, clicks and purchases
    # it has. A zombie session lasts more than 30 minutes, has
    # at least 5 scrolls, fewer than 0.20 clicks per scroll, and
    # no purchase at all. I order by scroll count descending,
    # then session id ascending.
    events = app_events.copy()
    events["event_timestamp"] = pd.to_datetime(events["event_timestamp"])
    rows = []
    for (session_id, user_id), group in events.groupby(["session_id", "user_id"], sort=False):
        duration_minutes = int((group["event_timestamp"].max() - group["event_timestamp"].min()).total_seconds() // 60)
        scroll_count = int((group["event_type"] == "scroll").sum())
        click_count = int((group["event_type"] == "click").sum())
        purchase_count = int((group["event_type"] == "purchase").sum())
        if (
            duration_minutes > 30
            and scroll_count >= 5
            and click_count / scroll_count < 0.20
            and purchase_count == 0
        ):
            rows.append({
                "session_id": session_id,
                "user_id": user_id,
                "session_duration_minutes": duration_minutes,
                "scroll_count": scroll_count,
            })
    result = pd.DataFrame(rows, columns=["session_id", "user_id", "session_duration_minutes", "scroll_count"])
    if result.empty:
        return result
    return result.sort_values(["scroll_count", "session_id"], ascending=[False, True]).reset_index(drop=True)
