class Solution:
    def fallingSquares(self, positions: list[list[int]]) -> list[int]:
        # My thinking: each square lands on the tallest square it
        # overlaps, so track every landed square's span and height
        # and take the running maximum.
        placed = []  # (left, right, height)
        answer = []
        tallest = 0
        for left, side in positions:
            right = left + side
            base = 0
            for l, r, h in placed:
                if l < right and left < r:  # overlaps
                    base = max(base, h)
            height = base + side
            placed.append((left, right, height))
            tallest = max(tallest, height)
            answer.append(tallest)
        return answer
