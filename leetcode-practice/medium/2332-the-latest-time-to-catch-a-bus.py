# LeetCode 2332. The Latest Time to Catch a Bus — Medium
# https://leetcode.com/problems/the-latest-time-to-catch-a-bus/
# Submission 2204702164 — Accepted, Python3
#
# My thinking: sort both lists and simulate boarding — earliest passengers
# first, each bus taking up to `capacity` passengers who arrived by its
# time. If the last bus still has room, I can arrive at its departure
# time; otherwise I must arrive just before the last passenger who
# boarded it. Then step down while the time clashes with a real
# passenger's arrival, since I cannot arrive at exactly their time.
class Solution:
    def latestTimeCatchTheBus(self, buses: list[int], passengers: list[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()
        pset = set(passengers)
        j = 0
        last_boarded = -1
        boarded = 0
        for bus in buses:
            boarded = 0
            while boarded < capacity and j < len(passengers) and passengers[j] <= bus:
                last_boarded = passengers[j]
                j += 1
                boarded += 1
        if boarded < capacity:
            ans = buses[-1]
        else:
            ans = last_boarded - 1
        while ans in pset:
            ans -= 1
        return ans
