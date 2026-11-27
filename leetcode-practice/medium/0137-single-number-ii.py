class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        # My thinking: count the set bits at each position — every number
        # that appears three times contributes a multiple of 3 to each bit
        # count, so the leftover bits (count % 3) are exactly the single
        # number's bits. Rebuild it and fix the sign for negatives.
        result = 0
        for bit in range(32):
            count = sum((num >> bit) & 1 for num in nums)
            if count % 3:
                result |= 1 << bit
        # handle the sign bit for negative answers
        if result >= 1 << 31:
            result -= 1 << 32
        return result
