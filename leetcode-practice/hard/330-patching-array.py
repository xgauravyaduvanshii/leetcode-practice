class Solution:
    def minPatches(self, nums: list[int], n: int) -> int:
        # My thinking: if I can already build every value below
        # miss, then a number up to miss extends the reach to
        # miss + num; otherwise patching in miss itself doubles it.
        patches = 0
        miss = 1
        i = 0
        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                miss += miss
                patches += 1
        return patches
