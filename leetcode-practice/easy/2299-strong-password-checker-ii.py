# LeetCode 2299. Strong Password Checker II — Easy
# https://leetcode.com/problems/strong-password-checker-ii/
# Submission 2197621999 — Accepted, Python3
#
# My thinking: the password must be at least 8
# characters, have a lower and an upper case letter,
# a digit and a special character, and no two
# adjacent characters the same. I check all of that
# in one pass.

class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False
        special = set("!@#$%^&*()-+")
        has_lower = has_upper = has_digit = has_special = False
        for i, ch in enumerate(password):
            if i > 0 and password[i] == password[i - 1]:
                return False
            if ch.islower():
                has_lower = True
            elif ch.isupper():
                has_upper = True
            elif ch.isdigit():
                has_digit = True
            elif ch in special:
                has_special = True
        return has_lower and has_upper and has_digit and has_special
