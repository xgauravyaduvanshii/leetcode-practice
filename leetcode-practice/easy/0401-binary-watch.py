# LeetCode 401. Binary Watch — Easy
# https://leetcode.com/problems/binary-watch/
# Submission 2197471149 — Accepted, Python3
#
# My thinking: there are only 12 hours and 60 minutes,
# so I can just try them all. A time works if the
# number of 1 bits in the hour plus the number of 1
# bits in the minute equals the number of LEDs that
# are on. I format the minute with a leading zero.

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> list[str]:
        result = []
        for hour in range(12):
            for minute in range(60):
                if bin(hour).count("1") + bin(minute).count("1") == turnedOn:
                    result.append(f"{hour}:{minute:02d}")
        return result
