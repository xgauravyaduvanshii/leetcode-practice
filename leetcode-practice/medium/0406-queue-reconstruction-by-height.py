# LeetCode 406. Queue Reconstruction by Height — Medium
# https://leetcode.com/problems/queue-reconstruction-by-height/
# Submission 2198782553 — Accepted, Python3
#
# My thinking: I sort people tallest first, and
# among equals the one with fewer people in front
# first. Then I insert each person at the position
# their k says — everyone already standing is at
# least as tall, so the count in front stays right.

from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda person: (-person[0], person[1]))
        queue = []
        for person in people:
            queue.insert(person[1], person)
        return queue
