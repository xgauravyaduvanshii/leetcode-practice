// LeetCode 3826. Minimum Partition Score — Hard
// https://leetcode.com/problems/minimum-partition-score/
// Submission 2203198601 — Accepted, Rust
//
// My thinking: prefix sums P turn a piece's value into
// S(S+1)/2 where S is a difference of two prefix sums, so
// dp[t][i] — the best score of splitting the first i
// numbers into t pieces — is (P[i]^2+P[i])/2 plus the
// minimum over split points j of dp[t-1][j] +
// (P[j]^2-P[j])/2 - P[i]*P[j]. For fixed j that is a line
// in x = P[i] with slope -P[j] and intercept dp[t-1][j] +
// (P[j]^2-P[j])/2. The numbers are positive, so the prefix
// sums — and the query points — strictly increase while
// the slopes strictly decrease, which is exactly the
// monotone convex hull trick: a vector holds the lower
// hull, lines are dropped from the back when a new line
// makes them useless and from the front once the next
// line beats them at the current query point. Each layer
// costs O(n). The redundancy test is cross-multiplied in
// i128: the products reach about 1e21, past the i64
// limit, while the scores themselves fit in i64.
impl Solution {
    pub fn min_partition_score(nums: Vec<i32>, k: i32) -> i64 {
        let n = nums.len();
        let k = k as usize;
        let mut pref = vec![0i64; n + 1];
        for i in 0..n {
            pref[i + 1] = pref[i] + nums[i] as i64;
        }
        let inf = i64::MAX / 4;
        let mut prev = vec![inf; n + 1];
        prev[0] = 0;
        for t in 1..=k {
            let mut cur = vec![inf; n + 1];
            // Lower hull of (slope, intercept) lines, slopes
            // strictly decreasing; head is the first live line.
            let mut hull: Vec<(i64, i64)> = Vec::new();
            let mut head = 0usize;
            for i in t..=n {
                let j = i - 1;
                // Add the line for split point j, if j can be
                // split into t-1 pieces at all.
                if prev[j] < inf {
                    let m = -pref[j];
                    let b = prev[j] + (pref[j] * pref[j] - pref[j]) / 2;
                    while hull.len() - head >= 2 {
                        let (m1, b1) = hull[hull.len() - 2];
                        let (m2, b2) = hull[hull.len() - 1];
                        // The middle line is useless exactly
                        // when its crossing with the first line
                        // is at or after its crossing with the
                        // new line: (b2-b1)/(m1-m2) >=
                        // (b-b2)/(m2-m), cross-multiplied in
                        // i128 (both denominators are positive).
                        if (b2 as i128 - b1 as i128) * (m2 as i128 - m as i128)
                            >= (b as i128 - b2 as i128) * (m1 as i128 - m2 as i128)
                        {
                            hull.pop();
                        } else {
                            break;
                        }
                    }
                    hull.push((m, b));
                }
                if hull.len() - head == 0 {
                    continue;
                }
                let x = pref[i];
                while hull.len() - head >= 2 {
                    let (m1, b1) = hull[head];
                    let (m2, b2) = hull[head + 1];
                    if m1 * x + b1 >= m2 * x + b2 {
                        head += 1;
                    } else {
                        break;
                    }
                }
                let (m, b) = hull[head];
                cur[i] = (pref[i] * pref[i] + pref[i]) / 2 + m * x + b;
            }
            prev = cur;
        }
        prev[n]
    }
}
