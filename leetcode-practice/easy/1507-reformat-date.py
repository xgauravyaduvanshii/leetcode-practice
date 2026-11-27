# LeetCode 1507. Reformat Date — Easy
# https://leetcode.com/problems/reformat-date/
# Submission 2197582929 — Accepted, Python3
#
# My thinking: I split the date into day, month and
# year. A small table turns the month name into
# its two-digit number, and I strip the "st"/"nd"/
# "rd"/"th" off the day and pad it to two digits.
# Then I join them as year-month-day.

class Solution:
    def reformatDate(self, date: str) -> str:
        months = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06",
                  "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}
        day, month, year = date.split()
        return year + "-" + months[month] + "-" + day[:-2].zfill(2)
