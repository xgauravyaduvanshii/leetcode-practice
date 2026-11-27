// LeetCode 1916. Count Ways to Build Rooms in an Ant Colony — Hard
// https://leetcode.com/problems/count-ways-to-build-rooms-in-an-ant-colony/
// Submission 2201234049 — Accepted, Rust
//
// My thinking: a room can only be built after its
// parent, so each subtree contributes its own
// number of orders — I merge children with the
// multinomial coefficient, counting the ways to
// interleave their build orders.

const MOD: i64 = 1_000_000_007;

fn mod_pow(mut base: i64, mut exp: i64) -> i64 {
    let mut res = 1i64;
    while exp > 0 {
        if exp & 1 == 1 {
            res = res * base % MOD;
        }
        base = base * base % MOD;
        exp >>= 1;
    }
    res
}

impl Solution {
    pub fn ways_to_build_rooms(prev_room: Vec<i32>) -> i32 {
        let n = prev_room.len();
        let mut children: Vec<Vec<usize>> = vec![Vec::new(); n];
        for i in 1..n {
            children[prev_room[i] as usize].push(i);
        }
        let mut fact = vec![1i64; n + 1];
        for i in 1..=n {
            fact[i] = fact[i - 1] * i as i64 % MOD;
        }
        let mut inv_fact = vec![1i64; n + 1];
        inv_fact[n] = mod_pow(fact[n], MOD - 2);
        for i in (1..=n).rev() {
            inv_fact[i - 1] = inv_fact[i] * i as i64 % MOD;
        }
        let mut order = vec![0usize];
        let mut stack = vec![0usize];
        while let Some(u) = stack.pop() {
            for &v in &children[u] {
                order.push(v);
                stack.push(v);
            }
        }
        let mut size = vec![0usize; n];
        let mut ways = vec![0i64; n];
        for &u in order.iter().rev() {
            let mut total = 0usize;
            let mut w = 1i64;
            for &v in &children[u] {
                total += size[v];
                w = w * ways[v] % MOD;
            }
            w = w * fact[total] % MOD;
            for &v in &children[u] {
                w = w * inv_fact[size[v]] % MOD;
            }
            size[u] = total + 1;
            ways[u] = w;
        }
        ways[0] as i32
    }
}
