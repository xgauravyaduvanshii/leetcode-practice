from collections import Counter


class Solution:
    def countTriplets(self, nums: list[int]) -> int:
        # My thinking: count how often each AND of two numbers
        # occurs, then each third number just needs an AND value
        # that shares no bit with it.
        pair_counts = Counter()
        for a in nums:
            for b in nums:
                pair_counts[a & b] += 1
        total = 0
        for num in nums:
            for and_value, count in pair_counts.items():
                if and_value & num == 0:
                    total += count
        return total
