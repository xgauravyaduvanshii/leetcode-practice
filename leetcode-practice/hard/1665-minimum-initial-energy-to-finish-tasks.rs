impl Solution {
    pub fn minimum_effort(mut tasks: Vec<Vec<i32>>) -> i32 {
        // My thinking: a task that demands a big cushion
        // before it starts should go first — so sort by how
        // much extra energy each task needs beyond its cost,
        // then add up the running bill.
        tasks.sort_by_key(|t| -(t[1] - t[0]));
        let mut need = 0;
        let mut spent = 0;
        for t in &tasks {
            need = need.max(spent + t[1]);
            spent += t[0];
        }
        need
    }
}
