class Solution:
    def tallestBillboard(self, rods: list[int]) -> int:
        # My thinking: track the best shorter side for every height
        # difference — each rod either joins the taller side, the
        # shorter side, or sits out.
        dp = {0: 0}
        for rod in rods:
            new = dict(dp)
            for diff, shorter in dp.items():
                new[diff + rod] = max(new.get(diff + rod, 0), shorter)
                new[abs(diff - rod)] = max(
                    new.get(abs(diff - rod), 0),
                    shorter + min(diff, rod),
                )
            dp = new
        return dp[0]
