class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        # My thinking: scan s1 again and again, tracking how far into
        # s2 we have matched; the (s2 position, s1 count) state must
        # eventually repeat, and the repeats let us skip whole cycles
        # at once.
        if n1 == 0:
            return 0
        s2_count = 0
        s2_index = 0
        seen = {}
        s1_count = 0
        while s1_count < n1:
            for ch in s1:
                if ch == s2[s2_index]:
                    s2_index += 1
                    if s2_index == len(s2):
                        s2_index = 0
                        s2_count += 1
            s1_count += 1
            if s2_index in seen:
                prev_s1, prev_s2 = seen[s2_index]
                cycle_s1 = s1_count - prev_s1
                cycle_s2 = s2_count - prev_s2
                if cycle_s1 > 0:
                    cycles = (n1 - s1_count) // cycle_s1
                    s2_count += cycles * cycle_s2
                    s1_count += cycles * cycle_s1
                    seen = {}
            else:
                seen[s2_index] = (s1_count, s2_count)
        return s2_count // n2
