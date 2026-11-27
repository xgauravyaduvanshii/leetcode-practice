class Solution:
    def containsNearbyAlmostDuplicate(self, nums: list[int], indexDiff: int, valueDiff: int) -> bool:
        # My thinking: numbers at most valueDiff apart must land in
        # the same bucket of width valueDiff + 1, or a neighbouring
        # one. Keep only the last indexDiff numbers in the buckets,
        # so any match found is close enough in both senses.
        if valueDiff < 0:
            return False
        width = valueDiff + 1
        buckets = {}
        for i, num in enumerate(nums):
            bucket = num // width
            if bucket in buckets:
                return True
            if bucket - 1 in buckets and abs(num - buckets[bucket - 1]) <= valueDiff:
                return True
            if bucket + 1 in buckets and abs(num - buckets[bucket + 1]) <= valueDiff:
                return True
            buckets[bucket] = num
            if i >= indexDiff:
                del buckets[nums[i - indexDiff] // width]
        return False
