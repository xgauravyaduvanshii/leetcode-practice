class Solution:
    def maxStudents(self, seats: list[list[str]]) -> int:
        # My thinking: each row is a bitmask of who sits where —
        # no neighbours in the row, no broken seats, and no one
        # diagonally above — then carry the best count forward
        # row by row.
        rows, cols = len(seats), len(seats[0])
        valid = []
        for r in range(rows):
            row_masks = []
            for mask in range(1 << cols):
                ok = True
                for c in range(cols):
                    if mask >> c & 1:
                        if seats[r][c] == "#":
                            ok = False
                            break
                        if c > 0 and mask >> (c - 1) & 1:
                            ok = False
                            break
                if ok:
                    row_masks.append(mask)
            valid.append(row_masks)
        dp = {0: 0}
        for r in range(rows):
            new_dp = {}
            for mask in valid[r]:
                count = bin(mask).count("1")
                for prev_mask, prev_val in dp.items():
                    if mask & (prev_mask << 1) == 0 and mask & (prev_mask >> 1) == 0:
                        new_dp[mask] = max(new_dp.get(mask, 0), prev_val + count)
            dp = new_dp
        return max(dp.values())
