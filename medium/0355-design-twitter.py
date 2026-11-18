# LeetCode 355. Design Twitter — Medium
# https://leetcode.com/problems/design-twitter/
# Submission 2198756502 — Accepted, Python3
#
# My thinking: every tweet gets a timestamp, and a
# user's feed is the ten newest tweets from themself
# and everyone they follow. I collect those tweets
# into a max-heap by time and pop the top ten.

import heapq
from collections import defaultdict
from typing import List


class Twitter:
    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.follows = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        users = self.follows[userId] | {userId}
        heap = []
        for user in users:
            for time, tweet_id in self.tweets[user]:
                heapq.heappush(heap, (-time, tweet_id))
        return [heapq.heappop(heap)[1] for _ in range(min(10, len(heap)))]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)
