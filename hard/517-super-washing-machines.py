class Solution:
    def findMinMoves(self, machines: list[int]) -> int:
        # My thinking: the dress count must average out, so each
        # machine either sends its own surplus away or passes the
        # running imbalance along — the answer is the worst of both
        # at any machine.
        total = sum(machines)
        n = len(machines)
        if total % n != 0:
            return -1
        target = total // n
        moves = 0
        balance = 0
        for count in machines:
            diff = count - target
            balance += diff
            moves = max(moves, abs(balance), diff)
        return moves
