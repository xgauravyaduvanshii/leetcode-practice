# LeetCode 860. Lemonade Change — Easy
# https://leetcode.com/problems/lemonade-change/
# Submission 2197536042 — Accepted, Python3
#
# My thinking: I keep count of the $5 and $10 bills
# in the till. A $5 needs no change. A $10 needs
# one $5 back. A $20 needs $15 — best to give one
# $10 and one $5 if I can, otherwise three $5s.
# If I cannot make change at any point, I fail.

class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        fives = tens = 0
        for bill in bills:
            if bill == 5:
                fives += 1
            elif bill == 10:
                if fives == 0:
                    return False
                fives -= 1
                tens += 1
            else:
                if tens > 0 and fives > 0:
                    tens -= 1
                    fives -= 1
                elif fives >= 3:
                    fives -= 3
                else:
                    return False
        return True
