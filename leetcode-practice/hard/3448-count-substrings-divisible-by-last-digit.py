# LeetCode 3448. Count Substrings Divisible By Last Digit — Hard
# https://leetcode.com/problems/count-substrings-divisible-by-last-digit/
# Submission 2202543214 — Accepted 699/699, Python3
class Solution:
    def countSubstrings(self, s: str) -> int:
        # My thinking: a substring counts only when it ends on its
        # divisor d, so I sweep once and handle each last digit by
        # what divisibility by d depends on. For d = 1, 2, 5 every
        # substring ending there works. For d = 3, 6, 9 it is the
        # digit sum, so I count matching prefix sums mod 3 or 9.
        # For d = 7, 10 has inverse 5 mod 7, so equal values of
        # prefix * 5^pos mark divisible substrings. For d = 4 only
        # the last two digits matter, and for d = 8 only the last
        # three, so I check those directly.
        digits = [ord(c) - 48 for c in s]
        ans = 0
        freq3 = {0: 1}
        freq9 = {0: 1}
        freq7 = {0: 1}
        sum3 = 0
        sum9 = 0
        t7 = 0
        pow5 = 1
        for j, d in enumerate(digits):
            sum3 = (sum3 + d) % 3
            sum9 = (sum9 + d) % 9
            pow5 = (pow5 * 5) % 7
            t7 = (t7 + d * pow5) % 7
            if d == 1 or d == 2 or d == 5:
                ans += j + 1
            elif d == 3 or d == 6:
                ans += freq3.get(sum3, 0)
            elif d == 9:
                ans += freq9.get(sum9, 0)
            elif d == 7:
                ans += freq7.get(t7, 0)
            elif d == 4:
                if j >= 1 and digits[j - 1] % 2 == 0:
                    ans += j + 1
                else:
                    ans += 1
            elif d == 8:
                ans += 1
                if j >= 1 and (2 * digits[j - 1]) % 8 == 0:
                    ans += 1
                if j >= 2 and (4 * digits[j - 2] + 2 * digits[j - 1]) % 8 == 0:
                    ans += j - 1
            freq3[sum3] = freq3.get(sum3, 0) + 1
            freq9[sum9] = freq9.get(sum9, 0) + 1
            freq7[t7] = freq7.get(t7, 0) + 1
        return ans
