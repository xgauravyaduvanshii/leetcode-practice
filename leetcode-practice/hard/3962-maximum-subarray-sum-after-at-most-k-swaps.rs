// LeetCode 3962. Maximum Subarray Sum After at Most K Swaps — Hard
// https://leetcode.com/problems/maximum-subarray-sum-after-at-most-k-swaps/
// Submission 2203485918 — Accepted, Rust
impl Solution {
    pub fn max_sum(nums: Vec<i32>, k: i32) -> i64 {
        // My thinking: a swap can only change a window by
        // taking one element out of it and bringing one
        // element in from outside, so for a fixed window
        // the best use of t swaps is to drop its t
        // smallest elements and bring in the t largest
        // elements from outside the window. The gain of the
        // j-th such swap falls as j grows, so the best t is
        // where the gains stop being positive. I keep that
        // t with four heaps while the window grows: the
        // smallest inside elements, the rest of the inside,
        // the largest outside elements, and the rest of the
        // outside. Each new right end moves one element
        // from outside to inside, and each new left end
        // rebuilds the heaps. Adjusting t is cheap in the
        // long run: a new element can only raise the best t
        // by one, and t can only fall as far as it rose.
        use std::cmp::Reverse;
        use std::collections::BinaryHeap;

        let n = nums.len();
        let k = k as usize;
        let a: Vec<i64> = nums.iter().map(|&x| x as i64).collect();
        let mut ans = i64::MIN / 4;
        for l in 0..n {
            // in_small: max-heap of the t smallest inside
            // elements; in_rest: min-heap of the other
            // inside elements; out_big: min-heap of the t
            // largest outside elements; out_rest: max-heap
            // of the other outside elements. loc tracks
            // which heap each index is in; removed marks
            // elements that left the outside lazily.
            let mut in_small: BinaryHeap<(i64, usize)> = BinaryHeap::new();
            let mut in_rest: BinaryHeap<Reverse<(i64, usize)>> = BinaryHeap::new();
            let mut out_big: BinaryHeap<Reverse<(i64, usize)>> = BinaryHeap::new();
            let mut out_rest: BinaryHeap<(i64, usize)> =
                (0..n).filter(|&i| i != l).map(|i| (a[i], i)).collect();
            let mut removed = vec![false; n];
            let mut loc = vec![3u8; n];
            in_rest.push(Reverse((a[l], l)));
            loc[l] = 1;
            let mut window_sum = a[l];
            let mut swaps = 0usize;
            let mut sum_small = 0i64;
            let mut sum_big = 0i64;

            let mut r = l;
            loop {
                // Rebalance the swap count: add pairs while
                // the next pair helps, drop pairs while the
                // last pair hurts.
                let cap = k.min(r - l + 1);
                while swaps < cap {
                    while let Some(&(_, u)) = out_rest.peek() {
                        if removed[u] {
                            out_rest.pop();
                        } else {
                            break;
                        }
                    }
                    let top_out = out_rest.peek().map(|&(v, _)| v);
                    let top_in = in_rest.peek().map(|&Reverse((v, _))| v);
                    match (top_out, top_in) {
                        (Some(ov), Some(iv)) if ov > iv => {
                            let (ov, u) = out_rest.pop().unwrap();
                            out_big.push(Reverse((ov, u)));
                            loc[u] = 2;
                            sum_big += ov;
                            let Reverse((iv, u2)) = in_rest.pop().unwrap();
                            in_small.push((iv, u2));
                            loc[u2] = 0;
                            sum_small += iv;
                            swaps += 1;
                        }
                        _ => break,
                    }
                }
                while swaps > 0 {
                    while let Some(&Reverse((_, u))) = out_big.peek() {
                        if removed[u] {
                            out_big.pop();
                        } else {
                            break;
                        }
                    }
                    let top_big = out_big.peek().map(|&Reverse((v, _))| v);
                    let top_small = in_small.peek().map(|&(v, _)| v);
                    match (top_big, top_small) {
                        (Some(bv), Some(sv)) if bv < sv => {
                            let Reverse((bv, u)) = out_big.pop().unwrap();
                            out_rest.push((bv, u));
                            loc[u] = 3;
                            sum_big -= bv;
                            let (sv, u2) = in_small.pop().unwrap();
                            in_rest.push(Reverse((sv, u2)));
                            loc[u2] = 1;
                            sum_small -= sv;
                            swaps -= 1;
                        }
                        _ => break,
                    }
                }
                ans = ans.max(window_sum - sum_small + sum_big);
                if r + 1 == n {
                    break;
                }
                r += 1;
                let x = a[r];
                // x leaves the outside.
                if loc[r] == 2 {
                    removed[r] = true;
                    sum_big -= x;
                    while let Some(&(_, u)) = out_rest.peek() {
                        if removed[u] {
                            out_rest.pop();
                        } else {
                            break;
                        }
                    }
                    if let Some((ov, u)) = out_rest.pop() {
                        out_big.push(Reverse((ov, u)));
                        loc[u] = 2;
                        sum_big += ov;
                    } else {
                        let (sv, u2) = in_small.pop().unwrap();
                        in_rest.push(Reverse((sv, u2)));
                        loc[u2] = 1;
                        sum_small -= sv;
                        swaps -= 1;
                    }
                } else {
                    removed[r] = true;
                }
                // x enters the inside.
                if swaps > 0 {
                    in_small.push((x, r));
                    sum_small += x;
                    let (sv, u) = in_small.pop().unwrap();
                    sum_small -= sv;
                    in_rest.push(Reverse((sv, u)));
                    loc[u] = 1;
                    loc[r] = if u != r { 0 } else { 1 };
                } else {
                    in_rest.push(Reverse((x, r)));
                    loc[r] = 1;
                }
                window_sum += x;
            }
        }
        ans
    }
}
