# LeetCode 726. Number of Atoms — Hard
# https://leetcode.com/problems/number-of-atoms/
# Submission 2198669529 — Accepted, Python3
#
# My thinking: I parse the formula with a small
# recursive reader. An atom is a capital letter plus
# its lowercase tail, with an optional number after
# it. A bracketed group is parsed the same way and
# then multiplied by the number after its closing
# bracket. The final counts come out alphabetised.

from collections import Counter


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        def parse(i):
            counts = Counter()
            while i < len(formula) and formula[i] != ")":
                if formula[i] == "(":
                    inner, i = parse(i + 1)
                    j = i
                    while j < len(formula) and formula[j].isdigit():
                        j += 1
                    mult = int(formula[i:j]) if j > i else 1
                    for atom, c in inner.items():
                        counts[atom] += c * mult
                    i = j
                else:
                    j = i + 1
                    while j < len(formula) and formula[j].islower():
                        j += 1
                    atom = formula[i:j]
                    k = j
                    while k < len(formula) and formula[k].isdigit():
                        k += 1
                    counts[atom] += int(formula[j:k]) if k > j else 1
                    i = k
            return counts, i + 1

        counts, _ = parse(0)
        return "".join(
            atom + (str(c) if c > 1 else "") for atom, c in sorted(counts.items())
        )
