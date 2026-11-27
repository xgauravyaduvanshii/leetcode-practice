# LeetCode 811. Subdomain Visit Count — Medium
# https://leetcode.com/problems/subdomain-visit-count/
# Submission 2198944020 — Accepted, Python3
#
# My thinking: every visit counts for the domain
# itself and for each of its parent domains, so I
# split each entry and add its count to every
# suffix of the domain.

from collections import Counter
from typing import List


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counts = Counter()
        for entry in cpdomains:
            visits, domain = entry.split()
            visits = int(visits)
            parts = domain.split(".")
            for i in range(len(parts)):
                counts[".".join(parts[i:])] += visits
        return [f"{count} {domain}" for domain, count in counts.items()]
