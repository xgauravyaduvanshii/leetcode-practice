# LeetCode 420. Strong Password Checker — Hard
# https://leetcode.com/problems/strong-password-checker/
# Submission 2198657788 — Accepted, Python3
#
# My thinking: first I count which character types
# are missing and which runs of three or more repeats
# need breaking. Short passwords just need the bigger
# of the two counts. Long ones must delete the extra
# characters first, and I spend those deletions where
# they cut a replacement — a run of length 3m needs
# one deletion, 3m+1 needs two, 3m+2 needs three.

class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        missing = 3
        if any(c.islower() for c in password):
            missing -= 1
        if any(c.isupper() for c in password):
            missing -= 1
        if any(c.isdigit() for c in password):
            missing -= 1

        runs = []
        run = 1
        for i in range(1, len(password) + 1):
            if i < len(password) and password[i] == password[i - 1]:
                run += 1
            else:
                if run >= 3:
                    runs.append(run)
                run = 1

        length = len(password)
        if length < 6:
            return max(missing, 6 - length)
        if length <= 20:
            return max(missing, sum(run // 3 for run in runs))

        deletions = length - 20
        for mod in (0, 1, 2):
            for i in range(len(runs)):
                if deletions == 0:
                    break
                if runs[i] >= 3 and runs[i] % 3 == mod:
                    take = min(deletions, mod + 1)
                    runs[i] -= take
                    deletions -= take
        replacements = sum(run // 3 for run in runs)
        return (length - 20) + max(missing, replacements)
