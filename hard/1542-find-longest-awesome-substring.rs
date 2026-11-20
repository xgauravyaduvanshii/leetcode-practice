use std::collections::HashMap;

impl Solution {
    pub fn longest_awesome(s: String) -> i32 {
        // My thinking: a stretch rearranges into a palindrome
        // when at most one digit appears an odd number of times
        // — so track the parity mask and remember where each
        // mask first showed up.
        let mut first: HashMap<i32, i32> = HashMap::new();
        first.insert(0, -1);
        let mut mask = 0i32;
        let mut best = 0i32;
        for (i, b) in s.bytes().enumerate() {
            mask ^= 1 << (b - b'0');
            if let Some(&j) = first.get(&mask) {
                best = best.max(i as i32 - j);
            }
            for d in 0..10 {
                let other = mask ^ (1 << d);
                if let Some(&j) = first.get(&other) {
                    best = best.max(i as i32 - j);
                }
            }
            first.entry(mask).or_insert(i as i32);
        }
        best
    }
}
