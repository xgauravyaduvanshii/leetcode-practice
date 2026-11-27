class Solution:
    def twoEggDrop(self, n: int) -> int:
        # My thinking: with two eggs, m drops can cover
        # m + (m-1) + ... + 1 floors — so keep adding drops
        # until the floors covered reach n.
        moves = 1
        while moves * (moves + 1) // 2 < n:
            moves += 1
        return moves
