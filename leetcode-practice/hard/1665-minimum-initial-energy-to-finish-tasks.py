class Solution:
    def minimumEffort(self, tasks: list[list[int]]) -> int:
        # My thinking: a task that demands a big cushion
        # before it starts should go first — so sort by how
        # much extra energy each task needs beyond its cost,
        # then add up the running bill.
        tasks.sort(key=lambda t: t[1] - t[0], reverse=True)
        need = 0
        spent = 0
        for actual, minimum in tasks:
            need = max(need, spent + minimum)
            spent += actual
        return need
