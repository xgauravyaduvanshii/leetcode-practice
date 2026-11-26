// LeetCode 4068. Maximize Meeting Earnings with Idle Gaps — Hard
// https://leetcode.com/problems/maximize-meeting-earnings-with-idle-gaps/
// Submission 2203593388 — Accepted, Rust
//
// My thinking: sort by end time, so any meeting
// that can come before meeting i is an earlier
// index. Let dp[i] be the best total for a
// schedule whose last meeting is i. Taking i
// alone earns revenue[i]; extending a schedule
// ending at j (end[j] <= start[i], half-open so
// touching is allowed) adds revenue[i] plus the
// idle gap start[i] - end[j]. That is revenue[i]
// + start[i] + (dp[j] - end[j]), so for each i
// we only need the best value of dp[j] - end[j]
// over all eligible j. Because ends are sorted,
// the eligible j are a prefix, found by binary
// search, and their best dp[j] - end[j] is a
// running prefix maximum. The answer is the
// best dp over all i.
impl Solution {
    pub fn max_earnings(meetings: Vec<Vec<i32>>) -> i64 {
        let mut ms = meetings;
        ms.sort_by_key(|m| m[1]);
        let n = ms.len();
        let ends: Vec<i64> = ms.iter().map(|m| m[1] as i64).collect();
        let mut pref = vec![0i64; n]; // pref[i] = max(dp[j] - end[j]) for j <= i
        let mut ans: i64 = 0;
        for i in 0..n {
            let s = ms[i][0] as i64;
            let e = ms[i][1] as i64;
            let r = ms[i][2] as i64;
            let j = ends.partition_point(|&end| end <= s);
            let mut best = r;
            if j > 0 {
                best = best.max(r + s + pref[j - 1]);
            }
            let val = best - e;
            pref[i] = if i == 0 { val } else { val.max(pref[i - 1]) };
            ans = ans.max(best);
        }
        ans
    }
}
