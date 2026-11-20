from collections import Counter


class Solution:
    def maxEqualFreq(self, nums: list[int]) -> int:
        # My thinking: scan the prefix, tracking how many values
        # sit at each frequency — a prefix works when removing
        # one element leaves every frequency equal.
        value_freq = Counter()
        freq_count = Counter()
        max_freq = 0
        best = 0
        for i, num in enumerate(nums):
            old = value_freq[num]
            if old:
                freq_count[old] -= 1
            value_freq[num] = old + 1
            freq_count[old + 1] += 1
            max_freq = max(max_freq, old + 1)
            length = i + 1
            if max_freq == 1:
                best = length
            elif freq_count[max_freq] == 1 and freq_count[max_freq - 1] * (max_freq - 1) + max_freq == length:
                best = length
            elif freq_count[1] == 1 and freq_count[max_freq] * max_freq + 1 == length:
                best = length
        return best
