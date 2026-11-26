# LeetCode 1981. Minimize the Difference Between Target and Chosen Elements — Medium
# https://leetcode.com/problems/minimize-the-difference-between-target-and-chosen-elements/
# Submission 2204090964 — Accepted, Python3

# My thinking:
# I must pick exactly one number from each row, so the only thing that
# matters after processing some rows is which totals I can reach. I keep
# a True/False table over all reachable sums: I start with only sum 0
# reachable, and for each new row I mark every old sum plus each number
# in that row as reachable. The biggest possible total is the sum of the
# largest number in each row, so the table stays small (at most 70 rows
# times 70 per number). Once every row is processed, I scan the reachable
# sums and return the smallest distance from the target.

class Solution:
    def minimizeTheDifference(self, mat: list[list[int]], target: int) -> int:
        max_sum = sum(max(row) for row in mat)
        dp = [False] * (max_sum + 1)
        dp[0] = True
        for row in mat:
            ndp = [False] * (max_sum + 1)
            for s in range(max_sum + 1):
                if dp[s]:
                    for x in row:
                        ndp[s + x] = True
            dp = ndp
        return min(abs(s - target) for s in range(max_sum + 1) if dp[s])


if __name__ == "__main__":
    sol = Solution()
    # Example 1: 1 + 4 + 8 = 13, exactly the target.
    assert sol.minimizeTheDifference([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 13) == 0
    # Example 2: only one choice per row, sum is 6, |6 - 100| = 94.
    assert sol.minimizeTheDifference([[1], [2], [3]], 100) == 94
    # Example 3: best single pick is 7, |7 - 6| = 1.
    assert sol.minimizeTheDifference([[1, 2, 9, 8, 7]], 6) == 1
    print("All samples passed.")
