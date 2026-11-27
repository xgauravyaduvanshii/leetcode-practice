// LeetCode 3225. Maximum Score From Grid Operations — Hard
// https://leetcode.com/problems/maximum-score-from-grid-operations/
// Submission 2202106048 — Accepted, Rust
//
// My thinking: I process the columns left
// to right, keeping for each pair of
// consecutive heights the best score so
// far. A column's score is the sum of its
// top entries down to the taller of its
// neighbours, so each transition needs
// only prefix and suffix maxima over the
// previous height — that keeps the whole
// DP quadratic per column.

struct Solution;

impl Solution {
    pub fn maximum_score(grid: Vec<Vec<i32>>) -> i64 {
        let n = grid.len();
        let mut col_pref: Vec<Vec<i64>> = Vec::new();
        for c in 0..n {
            let mut pref = vec![0i64; n + 1];
            let mut s: i64 = 0;
            for i in 0..n {
                s += grid[i][c] as i64;
                pref[i + 1] = s;
            }
            col_pref.push(pref);
        }
        let zero_pref = vec![0i64; n + 1];
        const NEG: i64 = -4_000_000_000_000_000_000;
        let mut dp_cur = vec![vec![NEG; n + 1]; n + 1];
        dp_cur[0][0] = 0;
        for c in 0..=n {
            let pref: &Vec<i64> = if c == 0 { &zero_pref } else { &col_pref[c - 1] };
            let mut dp_next = vec![vec![NEG; n + 1]; n + 1];
            for a in 0..=n {
                let pa = pref[a];
                let mut pref_max = vec![NEG; n + 2];
                let mut cur = NEG;
                for b in 0..=n {
                    if dp_cur[a][b] > cur { cur = dp_cur[a][b]; }
                    pref_max[b + 1] = cur;
                }
                let mut suff = vec![NEG; n + 2];
                cur = NEG;
                for b in (0..=n).rev() {
                    let vb = dp_cur[a][b];
                    if vb != NEG {
                        let mut v = vb;
                        if b > a { v += pref[b] - pa; }
                        if v > cur { cur = v; }
                    }
                    suff[b] = cur;
                }
                if c == n {
                    let h = 0usize;
                    let cand1 = suff[h];
                    let pm = pref_max[h];
                    let cand2 = if pm == NEG { NEG } else if h > a { pm + pref[h] - pa } else { pm };
                    dp_next[h][a] = if cand1 > cand2 { cand1 } else { cand2 };
                } else {
                    for h in 0..=n {
                        let cand1 = suff[h];
                        let pm = pref_max[h];
                        let cand2 = if pm == NEG { NEG } else if h > a { pm + pref[h] - pa } else { pm };
                        dp_next[h][a] = if cand1 > cand2 { cand1 } else { cand2 };
                    }
                }
            }
            dp_cur = dp_next;
        }
        *dp_cur[0].iter().max().unwrap()
    }
}
