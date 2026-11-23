// LeetCode 3139. Minimum Cost to Equalize Array — Hard
// https://leetcode.com/problems/minimum-cost-to-equalize-array/
// Submission 2202033357 — Accepted, Rust
//
// My thinking: for a fixed target the
// cheapest mix of single and paired
// increments is forced by how much the
// smallest element must rise: its lifts
// can only pair with lifts of other
// elements, so any surplus lifts are
// singles. I evaluate that cost at the
// current maximum and around the target
// where the pairing first becomes tight,
// and keep the cheapest.

struct Solution;

impl Solution {
    pub fn min_cost_to_equalize_array(nums: Vec<i32>, cost1: i32, cost2: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let n = nums.len() as i64;
        let mx = *nums.iter().max().unwrap() as i64;
        let mn = *nums.iter().min().unwrap() as i64;
        let total: i64 = nums.iter().map(|&x| x as i64).sum();
        if n == 1 {
            return 0;
        }
        let c1 = cost1 as i64;
        let c2 = cost2 as i64;
        if c2 >= 2 * c1 {
            let d: i64 = nums.iter().map(|&x| mx - x as i64).sum();
            return ((d * c1) % MOD) as i32;
        }
        let cost = |t: i64| -> i64 {
            let d = n * t - total;
            let mxd = t - mn;
            let excess = 2 * mxd - d;
            let (singles, pairs) = if excess > 0 {
                (excess, d - mxd)
            } else {
                (d & 1, (d - (d & 1)) / 2)
            };
            pairs * c2 + singles * c1
        };
        let mut ans = cost(mx);
        if n > 2 {
            let num = total - 2 * mn;
            let mut t1 = if num > 0 { (num + n - 3) / (n - 2) } else { mx };
            if t1 < mx {
                t1 = mx;
            }
            for t in [t1 - 1, t1, t1 + 1] {
                if t >= mx {
                    ans = ans.min(cost(t));
                }
            }
        }
        (ans % MOD) as i32
    }
}
