# LeetCode 1311. Get Watched Videos by Your Friends — Medium
# https://leetcode.com/problems/get-watched-videos-by-your-friends/
# Submission 2199028604 — Accepted, Python3
#
# My thinking: I walk the friendship graph out
# to exactly the given level, then count the
# videos those friends watched and sort them
# by count, breaking ties by name.

from collections import Counter, deque
from typing import List


class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        seen = {id}
        queue = deque([id])
        for _ in range(level):
            for _ in range(len(queue)):
                person = queue.popleft()
                for friend in friends[person]:
                    if friend not in seen:
                        seen.add(friend)
                        queue.append(friend)
        counts = Counter()
        for person in queue:
            counts.update(watchedVideos[person])
        return sorted(counts, key=lambda video: (counts[video], video))
