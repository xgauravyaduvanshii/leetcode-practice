# LeetCode 239. Sliding Window Maximum — Hard
# https://leetcode.com/problems/sliding-window-maximum/
# Submission 2198397488 — Accepted, Python3
#
# My thinking: I keep the candidates for the window
# maximum in a deque, in decreasing order. Each new
# number throws out every smaller number behind it
# — they can never be the maximum again — and any
# index that has slid out of the window leaves from
# the front. The front of the deque is always the
# current window's maximum.

from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = deque()
        answer = []
        for i, num in enumerate(nums):
            while window and window[0] <= i - k:
                window.popleft()
            while window and nums[window[-1]] < num:
                window.pop()
            window.append(i)
            if i >= k - 1:
                answer.append(nums[window[0]])
        return answer
