# 3386. Button with Longest Push Time (Easy)
# https://leetcode.com/problems/button-with-longest-push-time/
# Submission 2200009430 — Accepted, Python3
from typing import List


class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        # My thinking: each button's press lasts from
        # the previous event's time until its own. The
        # longest press wins, and if two tie, the
        # smaller button number wins.
        best_button = events[0][0]
        best_time = events[0][1]
        prev = 0
        for button, time in events:
            duration = time - prev
            if duration > best_time or (duration == best_time and button < best_button):
                best_button = button
                best_time = duration
            prev = time
        return best_button
