// LeetCode 2420. Find All Good Indices — Medium
// https://leetcode.com/problems/find-all-good-indices/
// Submission 2204860710 — Accepted, Rust
//
// My thinking: same idea as the Python version — precompute the
// non-increasing run ending at each index and the non-decreasing run
// starting at each index, then keep every i whose neighbours cover k.
impl Solution {
    pub fn good_indices(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let n = nums.len();
        let k = k as usize;
        let mut left = vec![1usize; n];
        for i in 1..n {
            if nums[i] <= nums[i - 1] {
                left[i] = left[i - 1] + 1;
            }
        }
        let mut right = vec![1usize; n];
        for i in (0..n - 1).rev() {
            if nums[i] <= nums[i + 1] {
                right[i] = right[i + 1] + 1;
            }
        }
        (k..n - k)
            .filter(|&i| left[i - 1] >= k && right[i + 1] >= k)
            .map(|i| i as i32)
            .collect()
    }
}
