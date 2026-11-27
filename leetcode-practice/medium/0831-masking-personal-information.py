# LeetCode 831. Masking Personal Information — Medium
# https://leetcode.com/problems/masking-personal-information/
# Submission 2198949132 — Accepted, Python3
#
# My thinking: an email shows its first letter,
# five stars, and its last letter, with the
# domain lowercased. A phone number shows the
# last four digits, with a country code of stars
# when there are extra digits.

class Solution:
    def maskPII(self, s: str) -> str:
        if "@" in s:
            name, domain = s.split("@")
            return f"{name[0].lower()}*****{name[-1].lower()}@{domain.lower()}"
        digits = "".join(ch for ch in s if ch.isdigit())
        local = "***-***-" + digits[-4:]
        if len(digits) == 10:
            return local
        return "+" + "*" * (len(digits) - 10) + "-" + local
