# LeetCode 2960. Count Tested Devices After Test Operations — Easy
# https://leetcode.com/problems/count-tested-devices-after-test-operations/
# Submission 2198704621 — Accepted, Python3
#
# My thinking: devices are tested in order, and each
# tested device drains one percent from every device
# after it. So a device gets tested exactly when its
# battery is still above the number of devices
# already tested before it.

from typing import List


class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        tested = 0
        for battery in batteryPercentages:
            if battery - tested > 0:
                tested += 1
        return tested
