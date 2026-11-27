# LeetCode 842. Split Array into Fibonacci Sequence — Medium
# https://leetcode.com/problems/split-array-into-fibonacci-sequence/
# Submission 2198952759 — Accepted, Python3
#
# My thinking: once the first two numbers are
# chosen, the rest of the sequence is forced.
# I try every valid pair of starting numbers —
# no leading zeros, at most ten digits each —
# and keep the first one that runs to the end.

from typing import List


class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        n = len(num)

        def build(first, second, start):
            sequence = [first, second]
            while start < n:
                nxt = first + second
                if nxt > 2 ** 31 - 1:
                    return []
                text = str(nxt)
                if num[start:start + len(text)] != text:
                    return []
                sequence.append(nxt)
                first, second = second, nxt
                start += len(text)
            return sequence if len(sequence) >= 3 else []

        for i in range(1, min(11, n)):
            first_text = num[:i]
            if len(first_text) > 1 and first_text[0] == "0":
                break
            first = int(first_text)
            for j in range(i + 1, min(i + 11, n)):
                second_text = num[i:j]
                if len(second_text) > 1 and second_text[0] == "0":
                    break
                second = int(second_text)
                result = build(first, second, j)
                if result:
                    return result
        return []
