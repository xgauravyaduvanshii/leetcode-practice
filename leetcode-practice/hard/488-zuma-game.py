from functools import lru_cache


class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        # My thinking: try every useful insertion — next to a ball of
        # the same colour, or three of a colour the board lacks —
        # collapse the board after each one, and remember the best
        # result for every board-plus-hand state.
        def collapse(s):
            while True:
                i = 0
                out = []
                changed = False
                while i < len(s):
                    j = i
                    while j < len(s) and s[j] == s[i]:
                        j += 1
                    if j - i >= 3:
                        changed = True
                    else:
                        out.append(s[i:j])
                    i = j
                s = "".join(out)
                if not changed:
                    return s

        @lru_cache(maxsize=None)
        def dfs(board_state, hand_state):
            if not board_state:
                return 0
            best = 6  # more balls than the hand can ever hold
            hand_list = list(hand_state)
            for i in range(len(board_state) + 1):
                for c in range(26):
                    if hand_list[c] == 0:
                        continue
                    colour = chr(c + 65)
                    useful = False
                    if i < len(board_state) and board_state[i] == colour:
                        useful = True
                    if i > 0 and board_state[i - 1] == colour:
                        useful = True
                    if colour not in board_state and hand_list[c] >= 3:
                        useful = True
                    if not useful:
                        continue
                    new_board = collapse(board_state[:i] + colour + board_state[i:])
                    hand_list[c] -= 1
                    sub = dfs(new_board, tuple(hand_list))
                    if sub < 6:
                        best = min(best, 1 + sub)
                    hand_list[c] += 1
            return best

        hand_count = [0] * 26
        for ch in hand:
            hand_count[ord(ch) - 65] += 1
        answer = dfs(board, tuple(hand_count))
        return -1 if answer == 6 else answer
