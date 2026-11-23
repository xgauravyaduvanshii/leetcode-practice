// LeetCode 2532. Time to Cross a Bridge — Hard
// https://leetcode.com/problems/time-to-cross-a-bridge/
// Submission 2201802699 — Accepted, Rust
//
// My thinking: the bridge is the only
// bottleneck, so I run the clock forward
// event by event — workers waiting to
// cross are ordered by how slow they are,
// the right side always goes first, and
// nobody new leaves the left once every
// box already has a carrier. A box counts
// as home the moment its carrier steps
// off the bridge on the left — the
// putting down after that does not add
// to the answer.

use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn find_crossing_time(n: i32, k: i32, time: Vec<Vec<i32>>) -> i32 {
        let n = n as usize;
        let k = k as usize;
        // efficiency key: larger (left+right, index) = less efficient = higher priority
        let key = |i: usize| (time[i][0] + time[i][2], i as i32);
        // wait lists: max-heap on the key
        let mut wait_left: BinaryHeap<((i32, i32), usize)> = (0..k)
            .map(|i| (key(i), i))
            .collect();
        let mut wait_right: BinaryHeap<((i32, i32), usize)> = BinaryHeap::new();
        // picking / putting / crossing_left: min-heaps on finish time
        let mut picking: BinaryHeap<(Reverse<i32>, usize)> = BinaryHeap::new();
        let mut putting: BinaryHeap<(Reverse<i32>, usize)> = BinaryHeap::new();
        let mut crossing_left: BinaryHeap<(Reverse<i32>, usize)> = BinaryHeap::new();
        let mut sent = 0usize;
        let mut arrived = 0usize;
        let mut now = 0i32;
        let mut bridge_free = 0i32;
        loop {
            while let Some(&(Reverse(f), _)) = picking.peek() {
                if f > now {
                    break;
                }
                let (_, w) = picking.pop().unwrap();
                wait_right.push((key(w), w));
            }
            while let Some(&(Reverse(f), _)) = putting.peek() {
                if f > now {
                    break;
                }
                let (_, w) = putting.pop().unwrap();
                wait_left.push((key(w), w));
            }
            while let Some(&(Reverse(f), _)) = crossing_left.peek() {
                if f > now {
                    break;
                }
                let (Reverse(finish), w) = crossing_left.pop().unwrap();
                arrived += 1;
                if arrived == n {
                    return finish;
                }
                putting.push((Reverse(finish + time[w][3]), w));
            }
            if now >= bridge_free {
                if let Some((_, w)) = wait_right.pop() {
                    bridge_free = now + time[w][2];
                    crossing_left.push((Reverse(bridge_free), w));
                } else if !wait_left.is_empty() && sent < n {
                    let (_, w) = wait_left.pop().unwrap();
                    bridge_free = now + time[w][0];
                    picking.push((Reverse(bridge_free + time[w][1]), w));
                    sent += 1;
                } else {
                    let mut cands: Vec<i32> = Vec::new();
                    if let Some(&(Reverse(f), _)) = picking.peek() {
                        cands.push(f);
                    }
                    if let Some(&(Reverse(f), _)) = putting.peek() {
                        cands.push(f);
                    }
                    if let Some(&(Reverse(f), _)) = crossing_left.peek() {
                        cands.push(f);
                    }
                    now = *cands.iter().min().unwrap();
                }
            } else {
                let mut cands: Vec<i32> = vec![bridge_free];
                if let Some(&(Reverse(f), _)) = picking.peek() {
                    cands.push(f);
                }
                if let Some(&(Reverse(f), _)) = putting.peek() {
                    cands.push(f);
                }
                if let Some(&(Reverse(f), _)) = crossing_left.peek() {
                    cands.push(f);
                }
                now = *cands.iter().min().unwrap();
            }
        }
    }
}
