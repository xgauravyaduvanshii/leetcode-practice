# LeetCode 2211. Count Collisions on a Road — Medium
# https://leetcode.com/problems/count-collisions-on-a-road/
# Submission 2204501654 — Accepted, Python3
#
# My thinking: cars driving left at the far left and cars driving right
# at the far right never meet anyone, so I strip those off. Every car
# that remains is stuck in the pile-up: each 'R' and each 'L' in the
# middle collides at least once, and stationary cars in between count
# once each as part of the pile, so the answer is just the count of 'R'
# plus 'L' left after trimming.
class Solution:
    def countCollisions(self, directions: str) -> int:
        directions = directions.lstrip('L').rstrip('R')
        return directions.count('R') + directions.count('L')
