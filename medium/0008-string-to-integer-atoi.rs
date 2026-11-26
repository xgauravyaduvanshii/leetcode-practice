// LeetCode 8. String to Integer (atoi) — Medium
// https://leetcode.com/problems/string-to-integer-atoi/
// Submission 2203802248 — Accepted, Rust

// My thinking: I skip leading spaces, read an optional sign, then
// collect digits until a non-digit shows up. I build the number digit
// by digit, clamping it to the 32-bit signed range as I go, so a huge
// input can never overflow past the limits.
impl Solution {
    pub fn my_atoi(s: String) -> i32 {
        let bytes = s.as_bytes();
        let n = bytes.len();
        let mut i = 0;
        while i < n && bytes[i] == b' ' {
            i += 1;
        }
        let mut sign: i64 = 1;
        if i < n && (bytes[i] == b'+' || bytes[i] == b'-') {
            if bytes[i] == b'-' {
                sign = -1;
            }
            i += 1;
        }
        let mut value: i64 = 0;
        while i < n && bytes[i].is_ascii_digit() {
            value = value * 10 + (bytes[i] - b'0') as i64;
            if value * sign > i32::MAX as i64 {
                return i32::MAX;
            }
            if value * sign < i32::MIN as i64 {
                return i32::MIN;
            }
            i += 1;
        }
        (value * sign) as i32
    }
}
