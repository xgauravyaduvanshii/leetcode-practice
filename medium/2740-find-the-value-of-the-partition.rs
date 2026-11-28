// LeetCode 2740. Find the Value of the Partition — Medium
// https://leetcode.com/problems/find-the-value-of-the-partition/
// Submission 2205225990 — Accepted, Rust
//
// My thinking: same idea as the Python version — sort, then
// the answer is the smallest gap between neighbouring values.
impl Solution {
    pub fn find_value_of_partition(mut nums: Vec<i32>) -> i32 {
        nums.sort();
        let mut ans = i32::MAX;
        for w in nums.windows(2) {
            ans = ans.min(w[1] - w[0]);
        }
        ans
    }
}
