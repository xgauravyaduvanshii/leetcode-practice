class Solution:
    def chalkReplacer(self, chalk: list[int], k: int) -> int:
        # My thinking: whole rounds repeat, so skip them all
        # at once — then walk the last round until the chalk
        # runs out on someone.
        k %= sum(chalk)
        for i, c in enumerate(chalk):
            if k < c:
                return i
            k -= c
        return 0
