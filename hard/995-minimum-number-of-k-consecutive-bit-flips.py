class Solution:
    def minKBitFlips(self, nums: list[int], k: int) -> int:
        # My thinking: sweep left to right, flipping whenever the
        # current bit is still 0 — a flip started here is the only
        # chance to fix this spot, and a difference array tracks
        # when each flip stops applying.
        n = len(nums)
        flipped = [0] * (n + 1)
        current = 0
        flips = 0
        for i in range(n):
            current += flipped[i]
            if (nums[i] + current) % 2 == 0:
                if i + k > n:
                    return -1
                flips += 1
                current += 1
                flipped[i + k] -= 1
        return flips
