class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        # My thinking: keep both the biggest and the smallest product ending
        # at each position — a negative number flips them, so the smallest
        # can become the biggest after multiplying by a negative.
        best = max_prod = min_prod = nums[0]
        for num in nums[1:]:
            if num < 0:
                max_prod, min_prod = min_prod, max_prod
            max_prod = max(num, max_prod * num)
            min_prod = min(num, min_prod * num)
            best = max(best, max_prod)
        return best
