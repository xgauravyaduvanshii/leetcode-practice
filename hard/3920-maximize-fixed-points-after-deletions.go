// LeetCode 3920. Maximize Fixed Points After Deletions — Hard
// https://leetcode.com/problems/maximize-fixed-points-after-deletions/
// Submission 2203402393 — Accepted, Go
import "sort"

// My thinking: suppose the fixed points we end up with
// are at original indices i_1 < ... < i_m with values
// v_t = nums[i_t]. The t-th fixed point has new index
// v_t, so exactly v_t kept elements sit before it: the
// t - 1 earlier fixed points plus v_t - t + 1 fillers
// chosen from the indices before it. That is possible
// exactly when v_1 <= i_1 and, between consecutive fixed
// points, the v_{t+1} - v_t - 1 new fillers fit in the
// i_{t+1} - i_t - 1 slots between them. Writing
// d_t = v_t - i_t, both conditions are d_t <= 0 and
// d_{t+1} <= d_t. So the answer is the longest chain of
// points (v, d) with d <= 0, strictly increasing v and
// non-increasing d. The index order comes for free:
// v_j < v_i and d_j >= d_i force j = v_j - d_j <=
// v_j - d_i < i. I sort the points by value, query the
// best chain over d' >= d in a Fenwick tree for suffix
// maxima (reversed coordinate), and insert each value
// group only after querying it, so equal values never
// chain together.
func maxFixedPoints(nums []int) int {
	type point struct {
		v, d int
	}
	pts := make([]point, 0, len(nums))
	for i, v := range nums {
		if d := v - i; d <= 0 {
			pts = append(pts, point{v, d})
		}
	}
	if len(pts) == 0 {
		return 0
	}
	sort.Slice(pts, func(a, b int) bool { return pts[a].v < pts[b].v })
	ds := make([]int, 0, len(pts))
	seen := make(map[int]bool)
	for _, p := range pts {
		if !seen[p.d] {
			seen[p.d] = true
			ds = append(ds, p.d)
		}
	}
	sort.Ints(ds)
	comp := make(map[int]int, len(ds))
	for i, d := range ds {
		comp[d] = i + 1
	}
	m := len(ds)
	bit := make([]int, m+2)
	bitUpdate := func(i, v int) {
		for ; i <= m; i += i & -i {
			if v > bit[i] {
				bit[i] = v
			}
		}
	}
	bitQuery := func(i int) int {
		r := 0
		for ; i > 0; i -= i & -i {
			if bit[i] > r {
				r = bit[i]
			}
		}
		return r
	}
	ans := 0
	for idx := 0; idx < len(pts); {
		j := idx
		for j < len(pts) && pts[j].v == pts[idx].v {
			j++
		}
		type pending struct {
			d, chain int
		}
		pend := make([]pending, 0, j-idx)
		for t := idx; t < j; t++ {
			d := pts[t].d
			// Suffix max over d' >= d is a prefix max
			// over the reversed coordinate.
			chain := bitQuery(m-comp[d]+1) + 1
			if chain > ans {
				ans = chain
			}
			pend = append(pend, pending{d, chain})
		}
		for _, p := range pend {
			bitUpdate(m-comp[p.d]+1, p.chain)
		}
		idx = j
	}
	return ans
}
