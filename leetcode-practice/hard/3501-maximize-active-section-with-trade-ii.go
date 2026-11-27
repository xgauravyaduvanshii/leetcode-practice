// LeetCode 3501. Maximize Active Section with Trade II — Hard
// https://leetcode.com/problems/maximize-active-section-with-trade-ii/
// Submission 2202744096 — Accepted, Go
package main

func maxActiveSectionsAfterTrade(s string, queries [][]int) []int {
	// My thinking: the answer counts '1's in the whole string, so a
	// trade only adds the '0's it turns into '1's inside the queried
	// substring. A trade picks an interior '1'-block and turns the
	// two '0'-blocks next to it into '1's, gaining exactly those two
	// blocks' lengths (the '1'-block itself comes back). For a query
	// the gain of a '1'-block is the two neighbouring zero-runs cut
	// down to the query bounds. Only the first and the last interior
	// '1'-block can be cut at all: every middle block's runs lie
	// wholly inside the query, so its full value applies and the
	// best middle block is a range maximum over precomputed values.
	n := len(s)
	totalOnes := 0
	for i := 0; i < n; i++ {
		if s[i] == '1' {
			totalOnes++
		}
	}
	type block struct{ a, b, lz, rz int }
	blocks := []block{}
	for i := 0; i < n; {
		if s[i] == '1' {
			j := i
			for j+1 < n && s[j+1] == '1' {
				j++
			}
			lz := 0
			for k := i - 1; k >= 0 && s[k] == '0'; k-- {
				lz++
			}
			rz := 0
			for k := j + 1; k < n && s[k] == '0'; k++ {
				rz++
			}
			blocks = append(blocks, block{i, j, lz, rz})
			i = j + 1
		} else {
			i++
		}
	}
	ans := make([]int, len(queries))
	if len(blocks) == 0 {
		for i := range ans {
			ans[i] = totalOnes
		}
		return ans
	}
	m := len(blocks)
	aList := make([]int, m)
	bList := make([]int, m)
	full := make([]int, m)
	for i, bl := range blocks {
		aList[i] = bl.a
		bList[i] = bl.b
		full[i] = bl.lz + bl.rz
	}
	log := make([]int, m+1)
	for i := 2; i <= m; i++ {
		log[i] = log[i/2] + 1
	}
	st := [][]int{append([]int(nil), full...)}
	for j := 1; (1 << j) <= m; j++ {
		prev := st[len(st)-1]
		cur := make([]int, m-(1<<j)+1)
		for i := range cur {
			if prev[i] > prev[i+(1<<(j-1))] {
				cur[i] = prev[i]
			} else {
				cur[i] = prev[i+(1<<(j-1))]
			}
		}
		st = append(st, cur)
	}
	rangeMax := func(l, r int) int {
		if l > r {
			return 0
		}
		j := log[r-l+1]
		if st[j][l] > st[j][r-(1<<j)+1] {
			return st[j][l]
		}
		return st[j][r-(1<<j)+1]
	}
	bisectRight := func(xs []int, v int) int {
		lo, hi := 0, len(xs)
		for lo < hi {
			mid := (lo + hi) / 2
			if xs[mid] <= v {
				lo = mid + 1
			} else {
				hi = mid
			}
		}
		return lo
	}
	bisectLeft := func(xs []int, v int) int {
		lo, hi := 0, len(xs)
		for lo < hi {
			mid := (lo + hi) / 2
			if xs[mid] < v {
				lo = mid + 1
			} else {
				hi = mid
			}
		}
		return lo
	}
	for qi, q := range queries {
		l, r := q[0], q[1]
		first := bisectRight(aList, l)
		last := bisectLeft(bList, r) - 1
		if first > last {
			ans[qi] = totalOnes
			continue
		}
		gain := 0
		if first+1 <= last-1 {
			if v := rangeMax(first+1, last-1); v > gain {
				gain = v
			}
		}
		bl0 := blocks[first]
		right0 := bl0.rz
		if first == last {
			if v := r - bl0.b; v < right0 {
				right0 = v
			}
		}
		left0 := bl0.lz
		if v := bl0.a - l; v < left0 {
			left0 = v
		}
		if left0+right0 > gain {
			gain = left0 + right0
		}
		if last > first {
			bl1 := blocks[last]
			right1 := bl1.rz
			if v := r - bl1.b; v < right1 {
				right1 = v
			}
			if bl1.lz+right1 > gain {
				gain = bl1.lz + right1
			}
		}
		ans[qi] = totalOnes + gain
	}
	return ans
}
