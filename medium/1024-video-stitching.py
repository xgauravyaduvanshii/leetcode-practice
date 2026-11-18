# LeetCode 1024. Video Stitching — Medium
# https://leetcode.com/problems/video-stitching/
# Submission 2198988929 — Accepted, Python3
#
# My thinking: I greedily extend the covered
# part as far as I can with the clips that start
# within it. Each jump adds one clip, and if no
# clip reaches further, the video cannot be
# covered.

from typing import List


class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort()
        clips_used = 0
        current_end = 0
        farthest = 0
        i = 0
        while current_end < time:
            while i < len(clips) and clips[i][0] <= current_end:
                farthest = max(farthest, clips[i][1])
                i += 1
            if farthest == current_end:
                return -1
            current_end = farthest
            clips_used += 1
        return clips_used
