// LeetCode 3102. Minimize Manhattan Distances — Hard
// https://leetcode.com/problems/minimize-manhattan-distances/
// Submission 2201995085 — Accepted, Rust
//
// My thinking: in (x + y, x - y)
// coordinates the Manhattan distance is
// the larger of the two coordinate gaps.
// Removing one point can only shrink
// the answer if that point is an extreme
// in either coordinate, so I only try
// removing the two smallest and two
// largest in each — at most eight
// candidates — and keep the best.

struct Solution;

impl Solution {
    pub fn minimum_distance(points: Vec<Vec<i32>>) -> i32 {
        let n = points.len();
        let u: Vec<i32> = points.iter().map(|p| p[0] + p[1]).collect();
        let v: Vec<i32> = points.iter().map(|p| p[0] - p[1]).collect();
        let extremes = |arr: &Vec<i32>| -> (Vec<usize>, Vec<usize>) {
            let mut idx: Vec<usize> = (0..n).collect();
            idx.sort_by_key(|&i| arr[i]);
            (idx[..2].to_vec(), idx[n - 2..].to_vec())
        };
        let (min_u, max_u) = extremes(&u);
        let (min_v, max_v) = extremes(&v);
        let mut cand: Vec<usize> = Vec::new();
        for &i in min_u.iter().chain(max_u.iter()).chain(min_v.iter()).chain(max_v.iter()) {
            if !cand.contains(&i) {
                cand.push(i);
            }
        }
        let mut ans = i32::MAX;
        for &i in &cand {
            let umax = if max_u[1] != i { u[max_u[1]] } else { u[max_u[0]] };
            let umin = if min_u[0] != i { u[min_u[0]] } else { u[min_u[1]] };
            let vmax = if max_v[1] != i { v[max_v[1]] } else { v[max_v[0]] };
            let vmin = if min_v[0] != i { v[min_v[0]] } else { v[min_v[1]] };
            ans = ans.min((umax - umin).max(vmax - vmin));
        }
        ans
    }
}
