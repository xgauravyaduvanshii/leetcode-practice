class Solution:
    def reductionOperations(self, nums: list[int]) -> int:
        # My thinking: sort the numbers — every time the value
        # steps up, all the bigger numbers still need one more
        # reduction to come down to it.
        nums.sort()
        ops = 0
        n = len(nums)
        for i in range(1, n):
            if nums[i] != nums[i - 1]:
                ops += n - i
        return ops
