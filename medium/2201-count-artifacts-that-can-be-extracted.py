# LeetCode 2201. Count Artifacts That Can Be Extracted — Medium
# https://leetcode.com/problems/count-artifacts-that-can-be-extracted/
# Submission 2204497764 — Accepted, Python3
#
# My thinking: an artifact can be extracted only when every cell of its
# rectangle has been dug. I put all dug cells in a set, then check each
# artifact's rectangle cell by cell and count the ones with no missing
# cell.
class Solution:
    def digArtifacts(self, n: int, artifacts: list[list[int]], dig: list[list[int]]) -> int:
        dug = {(r, c) for r, c in dig}
        count = 0
        for r1, c1, r2, c2 in artifacts:
            ok = True
            for r in range(r1, r2 + 1):
                for c in range(c1, c2 + 1):
                    if (r, c) not in dug:
                        ok = False
                        break
                if not ok:
                    break
            if ok:
                count += 1
        return count
