class Solution:
    def longestDecomposition(self, text: str) -> int:
        # My thinking: grow a chunk from both ends until they
        # match — any first match is safe to take, so the greedy
        # walk is optimal.
        n = len(text)
        left, right = 0, n
        chunks = 0
        while left < right:
            length = 1
            while left + length <= right - length and text[left:left + length] != text[right - length:right]:
                length += 1
            if left + length > right - length:
                chunks += 1
                break
            chunks += 2
            left += length
            right -= length
        return chunks
