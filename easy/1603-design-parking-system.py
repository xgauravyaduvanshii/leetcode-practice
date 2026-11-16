# LeetCode 1603. Design Parking System — Easy
# https://leetcode.com/problems/design-parking-system/
# Submission 2197588891 — Accepted, Python3
#
# My thinking: I keep a count of free slots for each
# car size (1 = big, 2 = medium, 3 = small). When
# a car arrives, if a slot of its size is free I
# take one and return true, otherwise false.

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.slots = {1: big, 2: medium, 3: small}

    def addCar(self, carType: int) -> bool:
        if self.slots[carType] > 0:
            self.slots[carType] -= 1
            return True
        return False
