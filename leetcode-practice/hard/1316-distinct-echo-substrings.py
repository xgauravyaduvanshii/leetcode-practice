class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        # My thinking: an echo substring is two identical halves
        # back to back — try every split point and grow the
        # halves together, keeping the ones we have seen.
        n = len(text)
        seen = set()
        for mid in range(1, n):
            length = 1
            while mid - length >= 0 and mid + length - 1 < n:
                left = text[mid - length:mid]
                right = text[mid:mid + length]
                if left == right:
                    seen.add(left + right)
                length += 1
        return len(seen)
