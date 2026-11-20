class Solution:
    def atMostNGivenDigitSet(self, digits: list[str], n: int) -> int:
        # My thinking: count the shorter numbers first (every
        # combination counts), then walk the digits of n left to
        # right, branching on smaller choices at each spot.
        s = str(n)
        length = len(s)
        count = 0
        for l in range(1, length):
            count += len(digits) ** l
        for i, ch in enumerate(s):
            smaller = sum(1 for d in digits if d < ch)
            count += smaller * len(digits) ** (length - i - 1)
            if ch not in digits:
                break
            if i == length - 1:
                count += 1
        return count
