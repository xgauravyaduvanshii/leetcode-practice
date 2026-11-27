# 3917. Count Indices With Opposite Parity (Easy)
# https://leetcode.com/problems/count-indices-with-opposite-parity/
# Submission 2200087496 — Accepted, Python3
class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        # My thinking: walking from the right, I keep
        # how many odds and evens I have seen. Each
        # position's score is simply the count of the
        # opposite parity still ahead of it.
        n = len(nums)
        ans = [0] * n
        odds = 0
        evens = 0
        for i in range(n - 1, -1, -1):
            ans[i] = evens if nums[i] % 2 == 1 else odds
            if nums[i] % 2 == 1:
                odds += 1
            else:
                evens += 1
        return ans
