import heapq


class Solution:
    def isPossible(self, target: list[int]) -> bool:
        # My thinking: run the process backwards — the biggest
        # number was the last one built, so take away the sum
        # of the rest (in one jump with a remainder) until
        # everything is back down to 1.
        total = sum(target)
        heap = [-x for x in target]
        heapq.heapify(heap)
        while heap[0] < -1:
            biggest = -heapq.heappop(heap)
            rest = total - biggest
            if rest == 0 or biggest <= rest:
                return False
            new_val = biggest % rest
            if new_val == 0:
                new_val = rest
            total = rest + new_val
            heapq.heappush(heap, -new_val)
        return True
