class Solution:
    def bestRotation(self, nums: list[int]) -> int:
        # My thinking: each element scores for a range of rotations,
        # so mark those ranges on a difference array and sweep once
        # for the best total.
        n = len(nums)
        diff = [0] * (n + 1)
        for i, num in enumerate(nums):
            # nums[i] scores for rotation k when num <= (i - k) mod n,
            # i.e. k in [(i - n + 1) mod n, (i - num) mod n] (mod n).
            left = (i - n + 1) % n
            right = (i - num) % n
            if left <= right:
                diff[left] += 1
                diff[right + 1] -= 1
            else:
                diff[0] += 1
                diff[right + 1] -= 1
                diff[left] += 1
        best_k = 0
        best_score = -1
        score = 0
        for k in range(n):
            score += diff[k]
            if score > best_score:
                best_score = score
                best_k = k
        return best_k
