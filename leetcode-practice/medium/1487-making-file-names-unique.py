# LeetCode 1487. Making File Names Unique — Medium
# https://leetcode.com/problems/making-file-names-unique/
# Submission 2199860373 — Accepted, Python3
#
# My thinking: I remember each name and the
# next free number for it. A clash gets the
# smallest "(k)" suffix that is still free,
# and that new name is remembered too.

from typing import List


class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        used = {}
        result = []
        for name in names:
            if name not in used:
                used[name] = 1
                result.append(name)
            else:
                k = used[name]
                while f"{name}({k})" in used:
                    k += 1
                used[name] = k + 1
                used[f"{name}({k})"] = 1
                result.append(f"{name}({k})")
        return result
