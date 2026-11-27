// LeetCode 2040. Kth Smallest Product of Two Sorted Arrays — Hard
// https://leetcode.com/problems/kth-smallest-product-of-two-sorted-arrays/
// Submission 2201556882 — Accepted, Rust
//
// My thinking: I guess a value and count how
// many pairs multiply to no more than it — a
// positive first number caps the second from
// above, a negative one from below — then I
// narrow the guess until the count reaches k.

impl Solution {
    pub fn kth_smallest_product(nums1: Vec<i32>, nums2: Vec<i32>, k: i32) -> i64 {
        let m = nums2.len() as i64;
        let k = k as i64;
        // floor division by a positive divisor.
        fn floor_div(a: i64, b: i64) -> i64 {
            if a >= 0 {
                a / b
            } else {
                -((-a + b - 1) / b)
            }
        }
        let count_le = |x: i64| -> i64 {
            let mut cnt: i64 = 0;
            for &a in nums1.iter() {
                let a = a as i64;
                if a > 0 {
                    let t = floor_div(x, a);
                    cnt += nums2.partition_point(|&b| (b as i64) <= t) as i64;
                } else if a < 0 {
                    // ceil(x / a) = -floor(x / -a)
                    let t = -floor_div(x, -a);
                    cnt += m - nums2.partition_point(|&b| (b as i64) < t) as i64;
                } else {
                    if x >= 0 {
                        cnt += m;
                    }
                }
            }
            cnt
        };
        let mut lo: i64 = -10_000_000_000 - 5;
        let mut hi: i64 = 10_000_000_000 + 5;
        while lo < hi {
            // lo + (hi - lo) / 2, not (lo + hi) / 2: Rust's / truncates
            // toward zero, so (lo + hi) / 2 can equal hi for negative
            // sums and the search never closes.
            let mid = lo + (hi - lo) / 2;
            if count_le(mid) >= k {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        lo
    }
}
