from __future__ import annotations


class Solution:
    def findInMountainArray(self, target: int, mountain_arr: MountainArray) -> int:
        # My thinking: find the peak with binary search, then
        # search the rising side and the falling side separately
        # — every array read is cached, staying far under the
        # 100-call limit.
        cache = {}

        def get(i):
            if i not in cache:
                cache[i] = mountain_arr.get(i)
            return cache[i]

        length = mountain_arr.length()
        left, right = 0, length - 1
        while left < right:
            mid = (left + right) // 2
            if get(mid) < get(mid + 1):
                left = mid + 1
            else:
                right = mid
        peak = left
        left, right = 0, peak
        while left <= right:
            mid = (left + right) // 2
            value = get(mid)
            if value == target:
                return mid
            if value < target:
                left = mid + 1
            else:
                right = mid - 1
        left, right = peak, length - 1
        while left <= right:
            mid = (left + right) // 2
            value = get(mid)
            if value == target:
                return mid
            if value > target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
