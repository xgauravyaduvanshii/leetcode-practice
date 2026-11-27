class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        # My thinking: each pig can be in one of (rounds + 1) states
        # (which round it dies in, or never), so p pigs distinguish
        # (rounds + 1) ** p outcomes — take the smallest p that
        # covers all buckets.
        states = minutesToTest // minutesToDie + 1
        pigs = 0
        outcomes = 1
        while outcomes < buckets:
            outcomes *= states
            pigs += 1
        return pigs
