class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        # My thinking: a super-palindrome's root is itself a
        # palindrome, so build every palindromic root up to 10^9
        # and keep the ones whose square is also a palindrome.
        lo, hi = int(left), int(right)
        count = 0
        for half in range(1, 100000):
            s = str(half)
            for root in (int(s + s[-2::-1]), int(s + s[::-1])):
                square = root * root
                if square > hi:
                    continue
                if square >= lo and str(square) == str(square)[::-1]:
                    count += 1
        return count
