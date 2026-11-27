class Solution:
    def minSwap(self, nums1: list[int], nums2: list[int]) -> int:
        # My thinking: at each step I either keep the pair or swap
        # it — both choices cost at most one swap — and each choice
        # is only allowed if both sequences stay increasing.
        keep = 0      # no swap at i
        swap = 1      # swap at i
        for i in range(1, len(nums1)):
            new_keep = float("inf")
            new_swap = float("inf")
            # Keep i, keep i - 1.
            if nums1[i] > nums1[i - 1] and nums2[i] > nums2[i - 1]:
                new_keep = min(new_keep, keep)
                new_swap = min(new_swap, swap + 1)
            # Keep i, swap i - 1.
            if nums1[i] > nums2[i - 1] and nums2[i] > nums1[i - 1]:
                new_keep = min(new_keep, swap)
                new_swap = min(new_swap, keep + 1)
            keep, swap = new_keep, new_swap
        return min(keep, swap)
