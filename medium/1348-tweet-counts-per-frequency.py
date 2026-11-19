# LeetCode 1348. Tweet Counts Per Frequency — Medium
# https://leetcode.com/problems/tweet-counts-per-frequency/
# Submission 2199037086 — Accepted, Python3
#
# My thinking: each tweet's times stay sorted,
# so counting tweets inside a chunk is two
# binary searches. I walk the range chunk by
# chunk — a minute, an hour, or a day at a time.

from bisect import bisect_left, bisect_right
from collections import defaultdict
from typing import List


class TweetCounts:
    def __init__(self):
        self.tweets = defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        times = self.tweets[tweetName]
        times.insert(bisect_left(times, time), time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        delta = {"minute": 60, "hour": 3600, "day": 86400}[freq]
        times = self.tweets[tweetName]
        result = []
        start = startTime
        while start <= endTime:
            end = min(start + delta - 1, endTime)
            result.append(bisect_right(times, end) - bisect_left(times, start))
            start += delta
        return result
