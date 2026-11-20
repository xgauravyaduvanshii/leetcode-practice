class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        # My thinking: the zero-count of n! only grows in steps of
        # five, so binary-search for the first n reaching k — if it
        # lands exactly on k there are five such n, otherwise none.
        def zeros(n):
            count = 0
            while n:
                n //= 5
                count += n
            return count

        lo, hi = 0, 5 * (k + 1)
        while lo < hi:
            mid = (lo + hi) // 2
            if zeros(mid) < k:
                lo = mid + 1
            else:
                hi = mid
        return 5 if zeros(lo) == k else 0
