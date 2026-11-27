# LeetCode 2410. Maximum Matching of Players With Trainers — Medium
# https://leetcode.com/problems/maximum-matching-of-players-with-trainers/
# Submission 2204790588 — Accepted, Python3
#
# My thinking: sort both arrays, then greedily match the weakest
# unmatched player with the weakest trainer who can handle them. A
# trainer who is too weak for the current player is too weak for every
# later (stronger) player too, so skipping them is safe.
class Solution:
    def matchPlayersAndTrainers(self, players: list[int], trainers: list[int]) -> int:
        players.sort()
        trainers.sort()
        i = 0
        ans = 0
        for t in trainers:
            if i < len(players) and players[i] <= t:
                ans += 1
                i += 1
        return ans
