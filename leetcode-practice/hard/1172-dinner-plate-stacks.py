import heapq


class DinnerPlates:
    # My thinking: keep every stack that still has room in a
    # heap, so pushes always find the leftmost gap — and when a
    # pop empties a slot, its index goes back in the heap.
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stacks = []
        self.available = []

    def push(self, val: int) -> None:
        while self.available:
            index = heapq.heappop(self.available)
            if index < len(self.stacks) and len(self.stacks[index]) < self.capacity:
                self.stacks[index].append(val)
                if len(self.stacks[index]) < self.capacity:
                    heapq.heappush(self.available, index)
                return
        self.stacks.append([val])
        if self.capacity > 1:
            heapq.heappush(self.available, len(self.stacks) - 1)

    def pop(self) -> int:
        while self.stacks and not self.stacks[-1]:
            self.stacks.pop()
        if not self.stacks:
            return -1
        value = self.stacks[-1].pop()
        heapq.heappush(self.available, len(self.stacks) - 1)
        return value

    def popAtStack(self, index: int) -> int:
        if index >= len(self.stacks) or not self.stacks[index]:
            return -1
        value = self.stacks[index].pop()
        heapq.heappush(self.available, index)
        return value
