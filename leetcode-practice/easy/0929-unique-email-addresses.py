# LeetCode 929. Unique Email Addresses — Easy
# https://leetcode.com/problems/unique-email-addresses/
# Submission 2197542963 — Accepted, Python3
#
# My thinking: the domain never changes, but the
# local part does — everything after a '+' is
# ignored, and dots in the local part are ignored
# too. So I clean up each local part, put the
# domain back on, and count how many different
# addresses I end up with.

class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        seen = set()
        for email in emails:
            local, domain = email.split('@')
            local = local.split('+')[0].replace('.', '')
            seen.add(local + '@' + domain)
        return len(seen)
