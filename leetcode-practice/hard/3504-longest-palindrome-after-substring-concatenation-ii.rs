// LeetCode 3504. Longest Palindrome After Substring Concatenation II — Hard
// https://leetcode.com/problems/longest-palindrome-after-substring-concatenation-ii/
// Submission 2202754299 — Accepted, Rust
impl Solution {
    pub fn longest_palindrome(s: String, t: String) -> i32 {
        // My thinking: a palindrome made from a substring of s plus a
        // substring of t is either wholly inside one string, or it
        // spans both. When it spans, the outer part is a substring of
        // s matched against the reverse of a substring of t, and the
        // inner part that is left over must itself be a palindrome. So
        // I precompute, for every pair of suffixes of s and reversed t,
        // how far they match, and for every position in s the longest
        // palindromic substring starting there. For a match of length L
        // starting at i, the best spanning palindrome is the longest
        // palindromic middle I can put after any of the first L matched
        // characters, which is a range maximum over 2*y + best-pal(y).
        // The mirror case, with the palindromic middle inside t, is the
        // same computation run on the two reversed strings.
        fn pal_dp(u: &[u8]) -> Vec<Vec<bool>> {
            let n = u.len();
            let mut pal = vec![vec![false; n]; n];
            for i in 0..n {
                pal[i][i] = true;
            }
            for i in 0..n.saturating_sub(1) {
                pal[i][i + 1] = u[i] == u[i + 1];
            }
            for len in 3..=n {
                for i in 0..=n - len {
                    let j = i + len - 1;
                    pal[i][j] = u[i] == u[j] && pal[i + 1][j - 1];
                }
            }
            pal
        }
        fn longest_pal_sub(u: &[u8]) -> i32 {
            let pal = pal_dp(u);
            let mut best = 0;
            for i in 0..u.len() {
                for j in i..u.len() {
                    if pal[i][j] {
                        best = best.max((j - i + 1) as i32);
                    }
                }
            }
            best
        }
        fn pal_start(u: &[u8], pal: &[Vec<bool>]) -> Vec<i32> {
            let n = u.len();
            let mut g = vec![0; n + 1];
            for y in 0..n {
                let mut best = 0;
                for j in y..n {
                    if pal[y][j] {
                        best = best.max((j - y + 1) as i32);
                    }
                }
                g[y] = best;
            }
            g
        }
        fn lcp_table(a: &[u8], b: &[u8]) -> Vec<Vec<i32>> {
            let (na, nb) = (a.len(), b.len());
            let mut lcp = vec![vec![0; nb + 1]; na + 1];
            for i in (0..na).rev() {
                for j in (0..nb).rev() {
                    lcp[i][j] = if a[i] == b[j] { lcp[i + 1][j + 1] + 1 } else { 0 };
                }
            }
            lcp
        }
        fn spanning(a: &[u8], b: &[u8]) -> i32 {
            let (na, nb) = (a.len(), b.len());
            let revb: Vec<u8> = b.iter().rev().cloned().collect();
            let pal_a = pal_dp(a);
            let g = pal_start(a, &pal_a);
            let h: Vec<i32> = (0..=na).map(|y| 2 * y as i32 + g[y]).collect();
            let m = h.len();
            let mut log = vec![0; m + 1];
            for i in 2..=m {
                log[i] = log[i / 2] + 1;
            }
            let mut st = vec![h.clone()];
            let mut j = 1;
            while (1 << j) <= m {
                let prev = st.last().unwrap().clone();
                let mut cur = vec![0; m - (1 << j) + 1];
                for i in 0..cur.len() {
                    cur[i] = prev[i].max(prev[i + (1 << (j - 1))]);
                }
                st.push(cur);
                j += 1;
            }
            let lcp = lcp_table(a, &revb);
            let mut best = 0;
            for i in 0..na {
                for p in 0..nb {
                    let l = lcp[i][p] as usize;
                    if l == 0 {
                        continue;
                    }
                    let lo = i + 1;
                    let hi = (i + l).min(na);
                    if lo > hi {
                        continue;
                    }
                    let jj = log[hi - lo + 1];
                    let mx = st[jj][lo].max(st[jj][hi - (1 << jj) + 1]);
                    best = best.max(mx - 2 * i as i32);
                }
            }
            best
        }
        let s_bytes = s.as_bytes();
        let t_bytes = t.as_bytes();
        let mut ans = longest_pal_sub(s_bytes).max(longest_pal_sub(t_bytes));
        ans = ans.max(spanning(s_bytes, t_bytes));
        let rev_t: Vec<u8> = t_bytes.iter().rev().cloned().collect();
        let rev_s: Vec<u8> = s_bytes.iter().rev().cloned().collect();
        ans = ans.max(spanning(&rev_t, &rev_s));
        ans
    }
}
