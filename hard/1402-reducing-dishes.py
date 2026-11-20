class Solution:
    def maxSatisfaction(self, satisfaction: list[int]) -> int:
        # My thinking: cook the best dishes last — sort them,
        # then keep adding the next dish while the dishes
        # already chosen still earn more than they cost.
        satisfaction.sort()
        total = 0
        suffix = 0
        for i in range(len(satisfaction) - 1, -1, -1):
            suffix += satisfaction[i]
            if suffix <= 0:
                break
            total += suffix
        return total
