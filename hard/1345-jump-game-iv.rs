use std::collections::{HashMap, HashSet, VecDeque};

impl Solution {
    pub fn min_jumps(arr: Vec<i32>) -> i32 {
        // My thinking: breadth-first search from the start — the
        // neighbours are the two next to you plus every index
        // holding the same value, and each value's list is used
        // once so the walk never repeats itself.
        let n = arr.len();
        if n == 1 {
            return 0;
        }
        let mut same: HashMap<i32, Vec<usize>> = HashMap::new();
        for (i, &val) in arr.iter().enumerate() {
            same.entry(val).or_default().push(i);
        }
        let mut queue: VecDeque<(usize, i32)> = VecDeque::new();
        queue.push_back((0, 0));
        let mut seen: HashSet<usize> = HashSet::new();
        seen.insert(0);
        while let Some((i, steps)) = queue.pop_front() {
            for nxt in [i.wrapping_sub(1), i + 1] {
                if nxt < n && !seen.contains(&nxt) {
                    if nxt == n - 1 {
                        return steps + 1;
                    }
                    seen.insert(nxt);
                    queue.push_back((nxt, steps + 1));
                }
            }
            if let Some(list) = same.get_mut(&arr[i]) {
                for &nxt in list.iter() {
                    if !seen.contains(&nxt) {
                        if nxt == n - 1 {
                            return steps + 1;
                        }
                        seen.insert(nxt);
                        queue.push_back((nxt, steps + 1));
                    }
                }
                list.clear();
            }
        }
        -1
    }
}
