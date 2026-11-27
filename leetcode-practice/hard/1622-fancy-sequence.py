class Fancy:
    # My thinking: adding and multiplying everything at once
    # is lazy work — so remember the running add and multiply
    # and undo them only when a value is read out.
    MOD = 10 ** 9 + 7

    def __init__(self):
        self.nums = []
        self.add = 0
        self.mul = 1

    def append(self, val: int) -> None:
        self.nums.append((val - self.add) * pow(self.mul, self.MOD - 2, self.MOD) % self.MOD)

    def addAll(self, inc: int) -> None:
        self.add = (self.add + inc) % self.MOD

    def multAll(self, m: int) -> None:
        self.add = self.add * m % self.MOD
        self.mul = self.mul * m % self.MOD

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.nums):
            return -1
        return (self.nums[idx] * self.mul + self.add) % self.MOD
