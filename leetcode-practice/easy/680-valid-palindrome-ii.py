# 680. Valid Palindrome II (Easy)
# https://leetcode.com/problems/valid-palindrome-ii/
# Submission 2199963529 — Accepted, Python3
class Solution:
    def validPalindrome(self, s: str) -> bool:
        # My thinking: walk in from both ends while the
        # letters match. The first mismatch is the only
        # place a deletion can help, so try skipping the
        # left letter, then the right one — if either side
        # reads clean after that, the string works.
        def is_pal(left: int, right: int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return is_pal(left + 1, right) or is_pal(left, right - 1)
            left += 1
            right -= 1
        return True
