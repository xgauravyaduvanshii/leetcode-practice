// LeetCode 2401. Longest Nice Subarray — Medium
// https://leetcode.com/problems/longest-nice-subarray/
// Submission 2204784693 — Accepted, Rust
//
// My thinking: same idea as the Python version — a sliding window over
// the OR of used bits, dropping numbers from the left (XORing their
// bits out) whenever the new number clashes; the longest window wins.
impl Solution {
    pub fn longest_nice_subarray(nums: Vec<i32>) -> i32 {
        let mut used = 0i32;
        let mut left = 0usize;
        let mut ans = 0i32;
        for (right, &x) in nums.iter().enumerate() {
            while used & x != 0 {
                used ^= nums[left];
                left += 1;
            }
            used |= x;
            let len = (right - left + 1) as i32;
            if len > ans {
                ans = len;
            }
        }
        ans
    }
}
