class Solution:
    def longestDupSubstring(self, s: str) -> str:
        # My thinking: binary search the answer length, and for
        # each length check every substring's hash — a repeated
        # hash means a duplicate (verified against the real text).
        n = len(s)
        base = 26
        mod = 2 ** 63 - 1

        def find(length):
            if length == 0:
                return ""
            power = pow(base, length - 1, mod)
            current = 0
            for i in range(length):
                current = (current * base + ord(s[i]) - ord("a") + 1) % mod
            seen = {current: 0}
            for i in range(1, n - length + 1):
                current = (current - (ord(s[i - 1]) - ord("a") + 1) * power) % mod
                current = (current * base + ord(s[i + length - 1]) - ord("a") + 1) % mod
                if current in seen:
                    start = seen[current]
                    if s[start:start + length] == s[i:i + length]:
                        return s[i:i + length]
                else:
                    seen[current] = i
            return None

        low, high = 0, n
        answer = ""
        while low <= high:
            mid = (low + high) // 2
            found = find(mid)
            if found is not None:
                answer = found
                low = mid + 1
            else:
                high = mid - 1
        return answer
