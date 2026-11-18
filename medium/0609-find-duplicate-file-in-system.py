# LeetCode 609. Find Duplicate File in System — Medium
# https://leetcode.com/problems/find-duplicate-file-in-system/
# Submission 2198877163 — Accepted, Python3
#
# My thinking: files with the same content belong
# together, so I group every file path by the
# content written in brackets after its name and
# keep the groups with more than one file.

import re
from collections import defaultdict
from typing import List


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        by_content = defaultdict(list)
        for path in paths:
            parts = path.split(" ")
            directory = parts[0]
            for file in parts[1:]:
                name, content = re.match(r"(.+)\((.+)\)", file).groups()
                by_content[content].append(directory + "/" + name)
        return [group for group in by_content.values() if len(group) > 1]
