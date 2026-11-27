# LeetCode 2591. Distribute Money to Maximum Children — Easy
# https://leetcode.com/problems/distribute-money-to-maximum-children/
# Submission 2197807811 — Accepted, Python3
#
# My thinking: everyone gets $1 first. Then I hand
# out $7 at a time to make children get $8. Two
# traps: if the last child would be left with $4,
# one $8 child must give it back; and if everyone
# gets $8 but money is left over, one child has to
# take the extra, so one fewer child gets exactly $8.

class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money < children:
            return -1
        money -= children
        count = min(children, money // 7)
        money -= count * 7
        if count == children and money == 0:
            return count
        if count == children - 1 and money == 3:
            return count - 1
        if count == children:
            return count - 1
        return count
