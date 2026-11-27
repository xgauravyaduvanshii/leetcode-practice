// LeetCode 2092. Find All People With Secret — Hard
// https://leetcode.com/problems/find-all-people-with-secret/
// Submission 2201570951 — Accepted, Rust
//
// My thinking: meetings that share a time can
// pass the secret around among themselves, so I
// take each time-slice on its own, link everyone
// meeting then, and spread the secret from
// whoever already knows it before that slice.

use std::collections::{HashMap, HashSet, VecDeque};

impl Solution {
    pub fn find_all_people(n: i32, meetings: Vec<Vec<i32>>, first_person: i32) -> Vec<i32> {
        let mut know: HashSet<i32> = HashSet::new();
        know.insert(0);
        know.insert(first_person);
        let mut meetings = meetings;
        meetings.sort_by_key(|m| m[2]);
        let mut i = 0;
        while i < meetings.len() {
            let mut j = i;
            while j < meetings.len() && meetings[j][2] == meetings[i][2] {
                j += 1;
            }
            let mut graph: HashMap<i32, Vec<i32>> = HashMap::new();
            let mut people: HashSet<i32> = HashSet::new();
            for m in &meetings[i..j] {
                graph.entry(m[0]).or_default().push(m[1]);
                graph.entry(m[1]).or_default().push(m[0]);
                people.insert(m[0]);
                people.insert(m[1]);
            }
            let mut q: VecDeque<i32> = VecDeque::new();
            let mut seen: HashSet<i32> = HashSet::new();
            for &p in people.iter() {
                if know.contains(&p) {
                    q.push_back(p);
                    seen.insert(p);
                }
            }
            while let Some(u) = q.pop_front() {
                know.insert(u);
                if let Some(neigh) = graph.get(&u) {
                    for &v in neigh {
                        if !seen.contains(&v) {
                            seen.insert(v);
                            q.push_back(v);
                        }
                    }
                }
            }
            i = j;
        }
        let mut ans: Vec<i32> = know.into_iter().collect();
        ans.sort();
        ans
    }
}
