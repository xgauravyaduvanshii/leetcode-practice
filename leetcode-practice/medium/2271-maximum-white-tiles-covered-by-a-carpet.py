# LeetCode 2271. Maximum White Tiles Covered by a Carpet — Medium
# https://leetcode.com/problems/maximum-white-tiles-covered-by-a-carpet/
# Submission 2204612322 — Accepted, Python3
#
# My thinking: sort the tiles by their start. With prefix sums of tile
# lengths I can get the total white tiles covered by any run of whole
# tiles in O(1). For each tile I place the carpet so its left edge is
# that tile's start, binary-search the last tile that starts inside the
# carpet, add the whole tiles up to it plus the part of that last tile
# the carpet reaches, and keep the best total.
import bisect


class Solution:
    def maximumWhiteTiles(self, tiles: list[list[int]], carpetLen: int) -> int:
        tiles.sort()
        starts = [t[0] for t in tiles]
        pref = [0]
        for l, r in tiles:
            pref.append(pref[-1] + r - l + 1)
        ans = 0
        for i in range(len(tiles)):
            end = tiles[i][0] + carpetLen - 1
            k = bisect.bisect_right(starts, end) - 1
            covered = pref[k] - pref[i]
            covered += min(tiles[k][1], end) - tiles[k][0] + 1
            ans = max(ans, covered)
        return ans
