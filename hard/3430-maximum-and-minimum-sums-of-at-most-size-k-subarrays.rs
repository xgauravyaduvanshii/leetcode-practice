// LeetCode 3430. Maximum and Minimum Sums of at Most Size K Subarrays — Hard
// https://leetcode.com/problems/maximum-and-minimum-sums-of-at-most-size-k-subarrays/
// Submission 2202528488 — Accepted 684/684, Rust
//
// My thinking: each element contributes as the max (and
// separately as the min) of the subarrays it dominates.
// Monotonic stacks give its reach on both sides; with l
// left choices and r right choices, l*r pairs exist but
// those longer than k must go — if l+r-1 exceeds k by
// `extra`, exactly extra*(extra+1)/2 pairs are too long.
// I add each element's value times its count.
impl Solution {
    pub fn min_max_subarray_sum(nums: Vec<i32>, k: i32) -> i64 {
        fn contribution(nums: &Vec<i32>, k: i32, is_min: bool) -> i64 {
            let n = nums.len();
            let mut prev = vec![-1i32; n];
            let mut next = vec![n as i32; n];
            let mut st: Vec<usize> = Vec::new();
            for i in 0..n {
                while let Some(&top) = st.last() {
                    if (is_min && nums[top] >= nums[i])
                        || (!is_min && nums[top] <= nums[i])
                    {
                        st.pop();
                    } else {
                        break;
                    }
                }
                prev[i] = st.last().map(|&t| t as i32).unwrap_or(-1);
                st.push(i);
            }
            st.clear();
            for i in (0..n).rev() {
                while let Some(&top) = st.last() {
                    if (is_min && nums[top] > nums[i])
                        || (!is_min && nums[top] < nums[i])
                    {
                        st.pop();
                    } else {
                        break;
                    }
                }
                next[i] = st.last().map(|&t| t as i32).unwrap_or(n as i32);
                st.push(i);
            }
            let mut total: i64 = 0;
            for i in 0..n {
                let l = std::cmp::min(i as i64 - prev[i] as i64, k as i64);
                let r = std::cmp::min(next[i] as i64 - i as i64, k as i64);
                let extra = std::cmp::max(0, l + r - 1 - k as i64);
                let cnt = l * r - extra * (extra + 1) / 2;
                total += nums[i] as i64 * cnt;
            }
            total
        }
        contribution(&nums, k, true) + contribution(&nums, k, false)
    }
}
