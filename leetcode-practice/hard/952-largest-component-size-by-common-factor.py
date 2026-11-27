class Solution:
    def largestComponentSize(self, nums: list[int]) -> int:
        # My thinking: two numbers belong together when they share
        # a prime factor, so union each number with its factors and
        # take the biggest group.
        parent = {}

        def find(x):
            parent.setdefault(x, x)
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            parent[find(a)] = find(b)

        for num in nums:
            x = num
            d = 2
            while d * d <= x:
                if x % d == 0:
                    union(num, d)
                    while x % d == 0:
                        x //= d
                d += 1
            if x > 1:
                union(num, x)
        counts = {}
        for num in nums:
            root = find(num)
            counts[root] = counts.get(root, 0) + 1
        return max(counts.values())
