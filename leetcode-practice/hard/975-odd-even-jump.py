class Solution:
    def oddEvenJumps(self, arr: list[int]) -> int:
        # My thinking: from each spot the next odd jump goes to the
        # smallest value not below it and the next even jump to the
        # largest value not above it — both found with monotone
        # stacks, then walk backwards.
        n = len(arr)
        next_higher = [None] * n
        next_lower = [None] * n
        stack = []
        for i in sorted(range(n), key=lambda i: (arr[i], i)):
            while stack and stack[-1] < i:
                next_higher[stack.pop()] = i
            stack.append(i)
        stack = []
        for i in sorted(range(n), key=lambda i: (-arr[i], i)):
            while stack and stack[-1] < i:
                next_lower[stack.pop()] = i
            stack.append(i)
        odd = [False] * n
        even = [False] * n
        odd[-1] = even[-1] = True
        for i in range(n - 2, -1, -1):
            if next_higher[i] is not None:
                odd[i] = even[next_higher[i]]
            if next_lower[i] is not None:
                even[i] = odd[next_lower[i]]
        return sum(odd)
