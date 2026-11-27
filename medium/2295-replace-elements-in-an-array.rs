// LeetCode 2295. Replace Elements in an Array — Medium
// https://leetcode.com/problems/replace-elements-in-an-array/
// Submission 2204658547 — Accepted, Rust
//
// My thinking: same idea as the Python version — a hash map from value
// to index makes each replacement O(1): move the map entry from the old
// value to the new one and write the new value into the array in place.
impl Solution {
    pub fn array_change(mut nums: Vec<i32>, operations: Vec<Vec<i32>>) -> Vec<i32> {
        use std::collections::HashMap;
        let mut pos: HashMap<i32, usize> = nums.iter().enumerate().map(|(i, &v)| (v, i)).collect();
        for op in operations {
            let old = op[0];
            let new = op[1];
            let i = pos.remove(&old).unwrap();
            nums[i] = new;
            pos.insert(new, i);
        }
        nums
    }
}
