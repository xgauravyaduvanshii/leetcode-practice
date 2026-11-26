// LeetCode 39. Combination Sum — Medium
// https://leetcode.com/problems/combination-sum/
// Submission 2203820284 — Accepted, Rust

// My thinking: I build combinations with backtracking, always moving
// forward through the candidates so the same set is never built twice
// in a different order. At each step I either take the current number
// again (it can be reused) or move on to the next one; when the
// remaining target hits zero I have a valid combination, and when it
// goes below zero that branch is dead.
impl Solution {
    pub fn combination_sum(candidates: Vec<i32>, target: i32) -> Vec<Vec<i32>> {
        let mut ans = Vec::new();
        let mut combo = Vec::new();
        fn backtrack(
            candidates: &Vec<i32>,
            target: i32,
            start: usize,
            combo: &mut Vec<i32>,
            ans: &mut Vec<Vec<i32>>,
        ) {
            if target == 0 {
                ans.push(combo.clone());
                return;
            }
            if target < 0 {
                return;
            }
            for i in start..candidates.len() {
                combo.push(candidates[i]);
                backtrack(candidates, target - candidates[i], i, combo, ans);
                combo.pop();
            }
        }
        backtrack(&candidates, target, 0, &mut combo, &mut ans);
        ans
    }
}
