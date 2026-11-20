# 3602. Hexadecimal and Hexatrigesimal Conversion (Easy)
# https://leetcode.com/problems/hexadecimal-and-hexatrigesimal-conversion/
# Submission 2200032629 — Accepted, Python3
class Solution:
    def concatHex36(self, n: int) -> str:
        # My thinking: write n in base 16 and in base
        # 36, then stick the two strings together. Base
        # 36 uses 0-9 and then A-Z for the bigger
        # digits.
        def to_base(num: int, base: int) -> str:
            digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            if num == 0:
                return "0"
            out = ""
            while num > 0:
                out = digits[num % base] + out
                num //= base
            return out

        return to_base(n, 16) + to_base(n, 36)
