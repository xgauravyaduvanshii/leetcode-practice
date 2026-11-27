# LeetCode 2379. Minimum Recolors to Get K Consecutive Black Blocks — Easy
# https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/
# Submission 2197775981 — Accepted, Python3
#
# My thinking: I slide a window of length k over the
# string and count the white blocks inside it — that
# is how many recolors that window needs. The
# smallest count over all windows is the answer.

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        whites = sum(1 for ch in blocks[:k] if ch == 'W')
        best = whites
        for i in range(k, len(blocks)):
            if blocks[i] == 'W':
                whites += 1
            if blocks[i - k] == 'W':
                whites -= 1
            best = min(best, whites)
        return best
