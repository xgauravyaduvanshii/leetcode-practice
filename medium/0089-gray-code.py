class Solution:
    def grayCode(self, n: int) -> list[int]:
        # My thinking: build the code by reflection — the n-bit code is the
        # (n-1)-bit code followed by the same code reversed with a 1 bit
        # set at position n-1. Start from [0] and grow one bit at a time.
        result = [0]
        for i in range(n):
            result += [x | (1 << i) for x in reversed(result)]
        return result
