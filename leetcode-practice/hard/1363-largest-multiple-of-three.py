class Solution:
    def largestMultipleOfThree(self, digits: list[int]) -> str:
        # My thinking: the biggest number is the digits in
        # descending order — just drop the smallest digits
        # that fix the remainder when the sum is not a
        # multiple of three.
        digits = sorted(digits)

        def drop(residue, k):
            removed = 0
            kept = []
            for d in digits:
                if removed < k and d % 3 == residue:
                    removed += 1
                else:
                    kept.append(d)
            return kept, removed == k

        total = sum(digits)
        if total % 3 == 1:
            digits, ok = drop(1, 1)
            if not ok:
                digits, ok = drop(2, 2)
                if not ok:
                    return ""
        elif total % 3 == 2:
            digits, ok = drop(2, 1)
            if not ok:
                digits, ok = drop(1, 2)
                if not ok:
                    return ""
        if not digits:
            return ""
        if digits[-1] == 0:
            return "0"
        return "".join(str(d) for d in reversed(digits))
