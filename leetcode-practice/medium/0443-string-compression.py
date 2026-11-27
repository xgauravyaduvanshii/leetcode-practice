# LeetCode 443. String Compression — Medium
# https://leetcode.com/problems/string-compression/
# Submission 2198796577 — Accepted, Python3
#
# My thinking: I read each run of equal letters and
# write it back in place — the letter, then its
# count digit by digit when there is more than one.
# The write position never overtakes the read
# position, so the array is safe to reuse.

from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0
        read = 0
        while read < len(chars):
            char = chars[read]
            count = 0
            while read < len(chars) and chars[read] == char:
                read += 1
                count += 1
            chars[write] = char
            write += 1
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
        return write
