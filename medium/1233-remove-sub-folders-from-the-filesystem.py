# LeetCode 1233. Remove Sub-Folders from the Filesystem — Medium
# https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/
# Submission 2199016491 — Accepted, Python3
#
# My thinking: sorted folders put every parent
# right before its children. A folder is a
# sub-folder exactly when it starts with the
# last folder I kept, plus a slash.

from typing import List


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        result = []
        for path in folder:
            if result and path.startswith(result[-1] + "/"):
                continue
            result.append(path)
        return result
