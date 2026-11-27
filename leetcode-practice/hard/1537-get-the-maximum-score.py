class Solution:
    def maxSum(self, nums1: list[int], nums2: list[int]) -> int:
        # My thinking: walk both sorted lists together — at
        # every shared number you may switch, so take the
        # richer of the two stretches since the last switch.
        MOD = 10 ** 9 + 7
        i = j = 0
        sum1 = sum2 = 0
        total = 0
        n, m = len(nums1), len(nums2)
        while i < n and j < m:
            if nums1[i] < nums2[j]:
                sum1 += nums1[i]
                i += 1
            elif nums1[i] > nums2[j]:
                sum2 += nums2[j]
                j += 1
            else:
                total += max(sum1, sum2) + nums1[i]
                i += 1
                j += 1
                sum1 = sum2 = 0
        while i < n:
            sum1 += nums1[i]
            i += 1
        while j < m:
            sum2 += nums2[j]
            j += 1
        total += max(sum1, sum2)
        return total % MOD
