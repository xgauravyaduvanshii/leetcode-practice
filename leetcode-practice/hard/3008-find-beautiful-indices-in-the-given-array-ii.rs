// LeetCode 3008. Find Beautiful Indices in the Given Array II — Hard
// https://leetcode.com/problems/find-beautiful-indices-in-the-given-array-ii/
// Submission 2201882376 — Accepted, Rust
//
// My thinking: I find every place a
// and b occur with KMP, then for each
// occurrence of a I check by binary
// search whether an occurrence of b
// sits within k of it.

impl Solution {
    pub fn beautiful_indices(s: String, a: String, b: String, k: i32) -> Vec<i32> {
        fn positions(text: &[u8], pat: &[u8]) -> Vec<usize> {
            // Prefix function, then one left-to-right scan.
            let mut pi = vec![0usize; pat.len()];
            let mut j = 0;
            for i in 1..pat.len() {
                while j > 0 && pat[i] != pat[j] {
                    j = pi[j - 1];
                }
                if pat[i] == pat[j] {
                    j += 1;
                }
                pi[i] = j;
            }
            let mut found = Vec::new();
            let mut j = 0;
            for (i, &ch) in text.iter().enumerate() {
                while j > 0 && ch != pat[j] {
                    j = pi[j - 1];
                }
                if ch == pat[j] {
                    j += 1;
                }
                if j == pat.len() {
                    found.push(i + 1 - pat.len());
                    j = pi[j - 1];
                }
            }
            found
        }
        let a_pos = positions(s.as_bytes(), a.as_bytes());
        let b_pos = positions(s.as_bytes(), b.as_bytes());
        let mut ans = Vec::new();
        for &i in &a_pos {
            let lo = i.saturating_sub(k as usize);
            let t = b_pos.partition_point(|&x| x < lo);
            if t < b_pos.len() && b_pos[t] <= i + k as usize {
                ans.push(i as i32);
            }
        }
        ans
    }
}
