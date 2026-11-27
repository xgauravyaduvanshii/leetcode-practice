# LeetCode 301. Remove Invalid Parentheses — Hard
# https://leetcode.com/problems/remove-invalid-parentheses/
# Submission 2198402374 — Accepted, Python3
#
# My thinking: I remove one bracket at a time and
# look at everything that comes out, level by level
# — every string in a level has had the same number
# of brackets removed. The first level that holds
# any valid string has the answer, because nothing
# with fewer removals could be valid. I remember
# strings I have already seen so the same one is
# never queued twice.

from collections import deque
from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def is_valid(text: str) -> bool:
            balance = 0
            for ch in text:
                if ch == "(":
                    balance += 1
                elif ch == ")":
                    balance -= 1
                    if balance < 0:
                        return False
            return balance == 0

        seen = {s}
        queue = deque([s])
        while queue:
            level = list(queue)
            queue.clear()
            valid = [text for text in level if is_valid(text)]
            if valid:
                return valid
            for text in level:
                for i, ch in enumerate(text):
                    if ch in "()":
                        nxt = text[:i] + text[i + 1:]
                        if nxt not in seen:
                            seen.add(nxt)
                            queue.append(nxt)
        return [""]
