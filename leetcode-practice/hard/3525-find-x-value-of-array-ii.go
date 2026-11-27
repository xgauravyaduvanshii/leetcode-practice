// LeetCode 3525. Find X Value of Array II — Hard
// https://leetcode.com/problems/find-x-value-of-array-ii/
// Submission 2202801941 — Accepted, Go
package main

func resultArray(nums []int, k int, queries [][]int) []int {
	// My thinking: for one query the answer is how many prefixes
	// of nums[start:] have product equal to x mod k. A segment
	// tree node stores exactly what is needed to answer that for
	// any segment: its total product, and how many of its prefixes
	// have each product mod k. Merging two neighbours is cheap:
	// the right half's prefixes all get multiplied by the left
	// half's total product, so its counts shift into new residue
	// buckets. A query is then one suffix-range merge, and a point
	// update rebuilds O(log n) nodes.
	n := len(nums)
	size := 1
	for size < n {
		size *= 2
	}
	prod := make([]int, 2*size)
	dist := make([][]int, 2*size)
	for i := range dist {
		dist[i] = make([]int, k)
		prod[i] = 1
	}
	for i, v := range nums {
		prod[size+i] = v % k
		dist[size+i][v%k] = 1
	}
	combine := func(pi int, di []int, pj int, dj []int) (int, []int) {
		p := (pi * pj) % k
		d := make([]int, k)
		copy(d, di)
		for q := 0; q < k; q++ {
			if dj[q] != 0 {
				d[(pi*q)%k] += dj[q]
			}
		}
		return p, d
	}
	for i := size - 1; i >= 1; i-- {
		prod[i], dist[i] = combine(prod[2*i], dist[2*i], prod[2*i+1], dist[2*i+1])
	}
	ans := make([]int, 0, len(queries))
	for _, q := range queries {
		idx, value, start, x := q[0], q[1], q[2], q[3]
		i := size + idx
		prod[i] = value % k
		dist[i] = make([]int, k)
		dist[i][value%k] = 1
		for i /= 2; i >= 1; i /= 2 {
			prod[i], dist[i] = combine(prod[2*i], dist[2*i], prod[2*i+1], dist[2*i+1])
		}
		l := size + start
		r := size + n
		lp, ld := 1, make([]int, k)
		rp, rd := 1, make([]int, k)
		for l < r {
			if l&1 == 1 {
				lp, ld = combine(lp, ld, prod[l], dist[l])
				l++
			}
			if r&1 == 1 {
				r--
				rp, rd = combine(prod[r], dist[r], rp, rd)
			}
			l /= 2
			r /= 2
		}
		_, fd := combine(lp, ld, rp, rd)
		ans = append(ans, fd[x])
	}
	return ans
}
