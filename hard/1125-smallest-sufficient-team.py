class Solution:
    def smallestSufficientTeam(self, req_skills: list[str], people: list[list[str]]) -> list[int]:
        # My thinking: each person is a mask of the skills they
        # cover — grow the cheapest team for every mask, adding
        # one person at a time.
        skill_index = {skill: i for i, skill in enumerate(req_skills)}
        n = len(req_skills)
        full = (1 << n) - 1
        dp = [None] * (1 << n)
        dp[0] = []
        for person, skills in enumerate(people):
            mask = 0
            for skill in skills:
                if skill in skill_index:
                    mask |= 1 << skill_index[skill]
            if mask == 0:
                continue
            for state in range(1 << n):
                if dp[state] is None:
                    continue
                new_state = state | mask
                if dp[new_state] is None or len(dp[state]) + 1 < len(dp[new_state]):
                    dp[new_state] = dp[state] + [person]
        return dp[full]
