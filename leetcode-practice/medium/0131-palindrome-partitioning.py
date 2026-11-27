# LeetCode 131. Palindrome Partitioning — Medium
# https://leetcode.com/problems/palindrome-partitioning/
# Submission 2204031154 — Accepted, Python3
#
# My thinking:
# Backtracking over the string: at each position, try every possible
# end index and keep only the substrings that are palindromes.
# A substring is a palindrome when it reads the same forwards and
# backwards, so check s[start:end+1] against its reverse.
# When the start index reaches the end of the string, the current
# path is one complete partition, so save a copy of it.
# Otherwise, for each palindromic prefix starting at the current
# position, add it to the path, recurse from the next position, then
# remove it again (backtrack) to try the next split.
# Every valid partition is found exactly once, because each recursive
# step fixes the next piece of the partition.

from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result: List[List[str]] = []
        path: List[str] = []
        n = len(s)

        def backtrack(start: int) -> None:
            if start == n:
                result.append(path.copy())
                return
            for end in range(start, n):
                substring = s[start:end + 1]
                if substring == substring[::-1]:
                    path.append(substring)
                    backtrack(end + 1)
                    path.pop()

        backtrack(0)
        return result
