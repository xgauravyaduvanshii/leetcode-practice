// LeetCode 2449. Minimum Number of Operations to Make Arrays Similar — Hard
// https://leetcode.com/problems/minimum-number-of-operations-to-make-arrays-similar/
// Submission 2201750576 — Accepted, Go
//
// My thinking: an operation moves two
// units and never changes a number's
// parity, so odds only ever become odds
// and evens only evens — I sort each
// parity group on its own, add up how
// much too much each side holds, and
// every two units of excess is one move.

package main

import "sort"

func makeSimilar(nums []int, target []int) int {
	ans := 0
	for parity := 0; parity <= 1; parity++ {
		var a, b []int
		for _, x := range nums {
			if x%2 == parity {
				a = append(a, x)
			}
		}
		for _, x := range target {
			if x%2 == parity {
				b = append(b, x)
			}
		}
		sort.Ints(a)
		sort.Ints(b)
		excess := 0
		for i := range a {
			if a[i] > b[i] {
				excess += a[i] - b[i]
			}
		}
		ans += excess / 2
	}
	return ans
}
