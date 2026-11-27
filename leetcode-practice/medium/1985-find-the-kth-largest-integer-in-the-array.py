# LeetCode 1985. Find the Kth Largest Integer in the Array — Medium
# https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/
# Submission 2204095138 — Accepted, Python3
#
# My thinking: the numbers arrive as strings, so I cannot compare them
# as plain text — "10" would wrongly beat "9". A number with more digits
# is always bigger (there are no leading zeros, except "0" itself), and
# among same-length numbers plain lexicographic order is correct. So I
# sort the strings by (length, value) and take the k-th from the end.
class Solution:
    def kthLargestNumber(self, nums: list[str], k: int) -> str:
        nums.sort(key=lambda s: (len(s), s))
        return nums[-k]


if __name__ == "__main__":
    s = Solution()
    assert s.kthLargestNumber(["3", "6", "7", "10"], 4) == "3"
    assert s.kthLargestNumber(["2", "21", "12", "1"], 3) == "2"
    assert s.kthLargestNumber(["0", "0"], 2) == "0"
    print("All samples passed.")
