class Solution:
    def maxValueAfterReverse(self, nums: list[int]) -> int:
        # My thinking: reversing a subarray only changes the
        # two adjacencies at its ends — so try every way to
        # rewire an end, plus the best middle swap, which is
        # twice the gap between the biggest small end and the
        # smallest big end of any adjacent pair.
        n = len(nums)
        base = sum(abs(nums[i] - nums[i + 1]) for i in range(n - 1))
        best = base
        for i in range(1, n):
            best = max(best, base + abs(nums[0] - nums[i]) - abs(nums[i] - nums[i - 1]))
            best = max(best, base + abs(nums[n - 1] - nums[i - 1]) - abs(nums[i] - nums[i - 1]))
        biggest_small = max(min(nums[i], nums[i + 1]) for i in range(n - 1))
        smallest_big = min(max(nums[i], nums[i + 1]) for i in range(n - 1))
        best = max(best, base + 2 * (biggest_small - smallest_big))
        return best
