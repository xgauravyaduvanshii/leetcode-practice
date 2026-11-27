// 3480. Maximize Subarrays After Removing One Conflicting Pair (Hard)
// https://leetcode.com/problems/maximize-subarrays-after-removing-one-conflicting-pair/
// Submission 2202669667 -- Accepted, Go
package main

import "sort"

func maxSubarrays(n int, conflictingPairs [][]int) int {
	// My thinking: a subarray ending at r is bad exactly when its left end
	// is at or before the biggest left end a of a remaining pair whose
	// right end is at or before r, so with M(r) for that biggest left end
	// the number of bad subarrays is the sum of M(r). Removing a pair can
	// only help when it is the unique biggest left end for its right end
	// and that right end is a new record for M; the gain is how far M drops
	// over the stretch until the next record, never below the previous
	// record or the second-biggest left end for that right end. I take the
	// best such gain over all record pairs, or zero when no removal helps.
	byHi := make(map[int][]int)
	for _, p := range conflictingPairs {
		lo, hi := p[0], p[1]
		if lo > hi {
			lo, hi = hi, lo
		}
		byHi[hi] = append(byHi[hi], lo)
	}
	type info struct{ mx, cnt, second int }
	A := make(map[int]info)
	his := make([]int, 0, len(byHi))
	for hi, los := range byHi {
		sort.Ints(los)
		mx := los[len(los)-1]
		cnt := 0
		for i := len(los) - 1; i >= 0 && los[i] == mx; i-- {
			cnt++
		}
		second := 0
		if cnt < len(los) {
			second = los[len(los)-1-cnt]
		}
		A[hi] = info{mx, cnt, second}
		his = append(his, hi)
	}
	sort.Ints(his)
	totalBad := 0
	curMax := 0
	hiIdx := 0
	for r := 1; r <= n; r++ {
		for hiIdx < len(his) && his[hiIdx] == r {
			if A[his[hiIdx]].mx > curMax {
				curMax = A[his[hiIdx]].mx
			}
			hiIdx++
		}
		totalBad += curMax
	}
	records := []int{}
	cur := 0
	for _, hi := range his {
		if A[hi].mx > cur {
			records = append(records, hi)
			cur = A[hi].mx
		}
	}
	maxGain := 0
	for idx, hi := range records {
		X, cnt, second := A[hi].mx, A[hi].cnt, A[hi].second
		if cnt >= 2 {
			continue
		}
		prevRec := 0
		if idx > 0 {
			prevRec = A[records[idx-1]].mx
		}
		nxt := n + 1
		if idx+1 < len(records) {
			nxt = records[idx+1]
		}
		P := prevRec
		curR := hi
		gain := 0
		for _, h := range his {
			if h <= hi || h >= nxt {
				continue
			}
			if P < X {
				m := P
				if second > m {
					m = second
				}
				gain += (X - m) * (h - curR)
			}
			if A[h].mx > P {
				P = A[h].mx
			}
			curR = h
		}
		if P < X {
			m := P
			if second > m {
				m = second
			}
			gain += (X - m) * (nxt - curR)
		}
		if gain > maxGain {
			maxGain = gain
		}
	}
	total := n * (n + 1) / 2
	return total - totalBad + maxGain
}
