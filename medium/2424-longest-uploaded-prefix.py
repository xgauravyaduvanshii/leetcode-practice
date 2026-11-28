# LeetCode 2424. Longest Uploaded Prefix — Medium
# https://leetcode.com/problems/longest-uploaded-prefix/
# Submission 2204861425 — Accepted, Python3
#
# My thinking: keep the uploaded videos in a set and a pointer at the
# longest prefix so far. Uploads only add to the set; longest() walks
# the pointer forward while the next video is present, so each video
# moves the pointer at most once.
class LUPrefix:
    def __init__(self, n: int):
        self.seen = set()
        self.cur = 0

    def upload(self, video: int) -> None:
        self.seen.add(video)

    def longest(self) -> int:
        while self.cur + 1 in self.seen:
            self.cur += 1
        return self.cur
