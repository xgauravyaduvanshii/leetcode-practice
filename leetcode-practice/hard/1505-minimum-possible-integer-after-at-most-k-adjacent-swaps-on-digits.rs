impl Solution {
    pub fn min_integer(num: String, k: i32) -> String {
        // My thinking: at each step, pull forward the smallest
        // digit still within reach — a Fenwick tree tracks
        // which digits are left and how far each one has to
        // travel.
        let n = num.len();
        let digits: Vec<u8> = num.bytes().map(|b| b - b'0').collect();
        let mut queues: Vec<std::collections::VecDeque<usize>> = vec![std::collections::VecDeque::new(); 10];
        for (i, &d) in digits.iter().enumerate() {
            queues[d as usize].push_back(i);
        }
        let mut bit = vec![0i32; n + 1];
        let bit_add = |bit: &mut Vec<i32>, mut i: usize, delta: i32| {
            i += 1;
            while i <= n {
                bit[i] += delta;
                i += i & i.wrapping_neg();
            }
        };
        let bit_sum = |bit: &Vec<i32>, mut i: usize| -> i32 {
            let mut s = 0;
            while i > 0 {
                s += bit[i];
                i -= i & i.wrapping_neg();
            }
            s
        };
        for i in 0..n {
            bit_add(&mut bit, i, 1);
        }
        let mut out = String::new();
        let mut remaining = k;
        for _ in 0..n {
            for d in 0..10usize {
                if queues[d].is_empty() {
                    continue;
                }
                let pos = queues[d][0];
                let cost = bit_sum(&bit, pos);
                if cost <= remaining {
                    out.push((b'0' + d as u8) as char);
                    queues[d].pop_front();
                    bit_add(&mut bit, pos, -1);
                    remaining -= cost;
                    break;
                }
            }
        }
        out
    }
}
