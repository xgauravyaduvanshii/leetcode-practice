# LeetCode 468. Validate IP Address — Medium
# https://leetcode.com/problems/validate-ip-address/
# Submission 2198815581 — Accepted, Python3
#
# My thinking: an IPv4 address is four plain
# decimal parts from 0 to 255 with no leading
# zeros, and an IPv6 address is eight groups of up
# to four hex digits. Anything else is neither.

class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if "." in queryIP:
            parts = queryIP.split(".")
            if len(parts) != 4:
                return "Neither"
            for part in parts:
                if not part or len(part) > 3 or not part.isdigit():
                    return "Neither"
                if len(part) > 1 and part[0] == "0":
                    return "Neither"
                if int(part) > 255:
                    return "Neither"
            return "IPv4"
        if ":" in queryIP:
            parts = queryIP.split(":")
            if len(parts) != 8:
                return "Neither"
            hex_digits = "0123456789abcdefABCDEF"
            for part in parts:
                if not part or len(part) > 4:
                    return "Neither"
                if any(char not in hex_digits for char in part):
                    return "Neither"
            return "IPv6"
        return "Neither"
