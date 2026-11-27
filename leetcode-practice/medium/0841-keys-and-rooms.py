# LeetCode 841. Keys and Rooms — Medium
# https://leetcode.com/problems/keys-and-rooms/
# Submission 2198952488 — Accepted, Python3
#
# My thinking: starting from room 0, I follow
# every key I find. If the rooms I can reach are
# all of them, the answer is yes.

from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen = {0}
        stack = [0]
        while stack:
            room = stack.pop()
            for key in rooms[room]:
                if key not in seen:
                    seen.add(key)
                    stack.append(key)
        return len(seen) == len(rooms)
