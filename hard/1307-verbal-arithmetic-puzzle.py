from collections import Counter


class Solution:
    def isSolvable(self, words: list[str], result: str) -> bool:
        # My thinking: give each letter a weight from the column
        # it sits in, then try the letters heaviest first — and
        # a one-letter word may be zero, since a lone 0 is not
        # a leading zero.
        weight = Counter()
        for word in words:
            for i, ch in enumerate(reversed(word)):
                weight[ch] += 10 ** i
        for i, ch in enumerate(reversed(result)):
            weight[ch] -= 10 ** i
        letters = sorted(weight, key=lambda ch: -abs(weight[ch]))
        leading = set()
        for word in words:
            if len(word) > 1:
                leading.add(word[0])
        if len(result) > 1:
            leading.add(result[0])
        used = [False] * 10

        def dfs(i, total):
            if i == len(letters):
                return total == 0
            ch = letters[i]
            for d in range(10):
                if used[d]:
                    continue
                if d == 0 and ch in leading:
                    continue
                used[d] = True
                if dfs(i + 1, total + weight[ch] * d):
                    return True
                used[d] = False
            return False

        return dfs(0, 0)
