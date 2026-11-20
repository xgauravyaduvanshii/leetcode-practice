# 3921. Score Validator (Easy)
# https://leetcode.com/problems/score-validator/
# Submission 2200087873 — Accepted, Python3
class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        # My thinking: I add up the runs and the
        # extras one by one, counting the wickets as I
        # go — and I stop the moment the tenth wicket
        # falls.
        score = 0
        counter = 0
        for e in events:
            if e == "W":
                counter += 1
                if counter == 10:
                    break
            elif e in ("WD", "NB"):
                score += 1
            else:
                score += int(e)
        return [score, counter]
