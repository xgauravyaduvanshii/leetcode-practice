class Solution:
    def minNumberOperations(self, target: list[int]) -> int:
        # My thinking: raising a stretch costs the height of
        # its lowest point — so each step up from the previous
        # height adds exactly that rise to the bill.
        ops = target[0]
        for i in range(1, len(target)):
            if target[i] > target[i - 1]:
                ops += target[i] - target[i - 1]
        return ops
