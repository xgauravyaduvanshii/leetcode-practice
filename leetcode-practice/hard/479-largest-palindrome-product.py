class Solution:
    def largestPalindrome(self, n: int) -> int:
        # My thinking: the answer is a palindrome, so try palindromes
        # from the top down — build each from its first half — and
        # keep the first one that splits into two n-digit factors.
        if n == 1:
            return 9
        upper = 10 ** n - 1
        lower = 10 ** (n - 1)
        for left in range(upper, lower - 1, -1):
            palindrome = int(str(left) + str(left)[::-1])
            for factor in range(upper, lower - 1, -1):
                if factor * factor < palindrome:
                    break
                if palindrome % factor == 0:
                    other = palindrome // factor
                    if lower <= other <= upper:
                        return palindrome % 1337
        return -1
