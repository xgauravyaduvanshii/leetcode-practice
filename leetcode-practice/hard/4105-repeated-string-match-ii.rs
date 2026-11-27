// LeetCode 4105. Repeated String Match II — Hard
// https://leetcode.com/problems/repeated-string-match-ii/
// Submission 2203734873 — Accepted, Rust
impl Solution {
    pub fn repeated_string_match(a: String, b: String, x: i32, y: i32) -> bool {
        // My thinking: the target is b repeated y times,
        // sitting inside a repeated x times. Any match
        // must start at some offset inside one copy of a,
        // so only starting offsets 0..|a|-1 need checking.
        // At a fixed offset, the pair of indices
        // ((off + t) % |a|, t % |b|) repeats with period
        // lcm(|a|, |b|), so comparing the first
        // min(L, lcm) characters decides the whole match:
        // if they all line up, the pattern repeats
        // forever and the rest of the match follows.
        // If the target is longer than the whole repeated
        // a, it can never fit, so return false early.
        let ab = a.as_bytes();
        let bb = b.as_bytes();
        let a_len = ab.len() as i64;
        let b_len = bb.len() as i64;
        let n = a_len * x as i64;
        let l = b_len * y as i64;
        if l > n {
            return false;
        }
        let g = gcd(a_len, b_len);
        let lcm = a_len / g * b_len;
        let limit = l.min(lcm);
        for off in 0..a_len {
            if off + l > n {
                break;
            }
            let mut ok = true;
            for t in 0..limit {
                if ab[((off + t) % a_len) as usize] != bb[(t % b_len) as usize] {
                    ok = false;
                    break;
                }
            }
            if ok {
                return true;
            }
        }
        false
    }
}

fn gcd(mut a: i64, mut b: i64) -> i64 {
    while b != 0 {
        let r = a % b;
        a = b;
        b = r;
    }
    a
}
