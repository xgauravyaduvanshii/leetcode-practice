class Solution:
    def threeEqualParts(self, arr: list[int]) -> list[int]:
        # My thinking: the three parts must hold the same number of
        # ones, so split after the first third of the ones and after
        # the second third, then check the tails match.
        n = len(arr)
        ones = [i for i, v in enumerate(arr) if v == 1]
        if not ones:
            return [0, n - 1]
        if len(ones) % 3:
            return [-1, -1]
        third = len(ones) // 3
        first = ones[0]
        second = ones[third]
        third_start = ones[2 * third]
        length = n - third_start
        for a in (first, second):
            for t in range(length):
                if arr[a + t] != arr[third_start + t]:
                    return [-1, -1]
        return [first + length - 1, second + length]
