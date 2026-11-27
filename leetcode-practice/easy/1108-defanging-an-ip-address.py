# LeetCode 1108. Defanging an IP Address — Easy
# https://leetcode.com/problems/defanging-an-ip-address/
# Submission 2197557669 — Accepted, Python3
#
# My thinking: defanging just means replacing every
# dot with "[.]" so the address cannot be clicked
# by accident. One replace call does the whole job.

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")
