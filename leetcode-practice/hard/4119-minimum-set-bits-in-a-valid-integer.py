# LeetCode 4119. Minimum Set Bits in a Valid Integer — Hard
# https://leetcode.com/problems/minimum-set-bits-in-a-valid-integer/
# Submission 2203743920 — Accepted, Python3


class Solution:
    def minSetBits(self, nums: list[int], k: int) -> int:
        # My thinking: a window's AND has a bit set
        # exactly when that bit appears in all k
        # numbers of the window, so keep a per-bit
        # count over the sliding window (nums[i] <=
        # 10^5 < 2^17, so bits 0..16 are enough) and
        # maintain the window AND mask: a bit joins
        # the mask when its count reaches k and leaves
        # when it drops below k. If any window AND is
        # 0, no y can hit it, so return -1. Otherwise
        # collect the set of window ANDs; a candidate
        # y is valid exactly when no window AND is a
        # submask of FULL ^ y, i.e. y shares a bit
        # with every window AND. Run a SOS DP over
        # the 2^17 masks to mark every submask of
        # each window AND, then scan all y and keep
        # the smallest popcount among the valid ones.
        cnt = [0] * 17
        mask = 0
        ba = bytearray(16384)
        n = len(nums)
        for i in range(n):
            x = nums[i]
            while x:
                lb = x & -x
                b = lb.bit_length() - 1
                c = cnt[b] + 1
                cnt[b] = c
                if c == k:
                    mask |= lb
                x ^= lb
            if i >= k:
                x = nums[i - k]
                while x:
                    lb = x & -x
                    b = lb.bit_length() - 1
                    if cnt[b] == k:
                        mask &= ~lb
                    cnt[b] -= 1
                    x ^= lb
            if i >= k - 1:
                if mask == 0:
                    return -1
                ba[mask >> 3] |= 1 << (mask & 7)
        FULL = (1 << 17) - 1
        B = int.from_bytes(ba, 'little')
        total = 1 << 17
        for b in range(17):
            step = 1 << b
            unit = ((1 << step) - 1) << step
            mb = unit
            sh = step << 1
            while sh < total:
                mb |= mb << sh
                sh <<= 1
            B |= (B << step) & mb
        bad = B.to_bytes(total // 8, 'little')
        best = 18
        for y in range(total):
            m = FULL ^ y
            if not (bad[m >> 3] >> (m & 7)) & 1:
                c = y.bit_count()
                if c < best:
                    best = c
                    if best == 1:
                        break
        return best if best <= 17 else -1
