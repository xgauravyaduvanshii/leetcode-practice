from collections import defaultdict


class FreqStack:
    # My thinking: keep each value's frequency, and stack the
    # values by frequency — popping from the highest frequency
    # stack gives the most frequent, most recent value.
    def __init__(self):
        self.freq = defaultdict(int)
        self.group = defaultdict(list)
        self.maxfreq = 0

    def push(self, val: int) -> None:
        f = self.freq[val] + 1
        self.freq[val] = f
        if f > self.maxfreq:
            self.maxfreq = f
        self.group[f].append(val)

    def pop(self) -> int:
        val = self.group[self.maxfreq].pop()
        self.freq[val] -= 1
        if not self.group[self.maxfreq]:
            self.maxfreq -= 1
        return val
