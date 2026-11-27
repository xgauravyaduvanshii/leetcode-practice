class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        # My thinking: count the subarrays with at most k distinct
        # numbers, then subtract those with at most k - 1 — the
        # difference is exactly k.
        def at_most(limit):
            counts = {}
            distinct = 0
            total = 0
            left = 0
            for right, num in enumerate(nums):
                if counts.get(num, 0) == 0:
                    distinct += 1
                counts[num] = counts.get(num, 0) + 1
                while distinct > limit:
                    counts[nums[left]] -= 1
                    if counts[nums[left]] == 0:
                        distinct -= 1
                    left += 1
                total += right - left + 1
            return total

        return at_most(k) - at_most(k - 1)
