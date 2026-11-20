use std::collections::BinaryHeap;
use std::cmp::Reverse;

impl Solution {
    pub fn max_performance(n: i32, speed: Vec<i32>, efficiency: Vec<i32>, k: i32) -> i32 {
        // My thinking: take the engineers in efficiency order —
        // the current engineer's efficiency is the team's, so
        // keep the k fastest speeds seen so far and multiply.
        const MOD: i64 = 1_000_000_007;
        let mut order: Vec<usize> = (0..n as usize).collect();
        order.sort_by_key(|&i| Reverse(efficiency[i]));
        let mut heap: BinaryHeap<Reverse<i64>> = BinaryHeap::new();
        let mut speed_sum: i64 = 0;
        let mut best: i64 = 0;
        for &i in &order {
            heap.push(Reverse(speed[i] as i64));
            speed_sum += speed[i] as i64;
            if heap.len() > k as usize {
                speed_sum -= heap.pop().unwrap().0;
            }
            best = best.max(speed_sum * efficiency[i] as i64);
        }
        (best % MOD) as i32
    }
}
