// LeetCode 2344. Minimum Deletions to Make Array Divisible — Hard
// https://leetcode.com/problems/minimum-deletions-to-make-array-divisible/
// Submission 2201692041 — Accepted, Go
//
// My thinking: the smallest survivor must
// divide every number it has to cover, so
// it must divide their gcd — I sort the
// array, take the first number that does,
// and drop everything smaller than it.

package main

import "sort"

func gcd2344(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func minOperations(nums []int, numsDivide []int) int {
	g := 0
	for _, x := range numsDivide {
		g = gcd2344(g, x)
	}
	sort.Ints(nums)
	for i, x := range nums {
		if g%x == 0 {
			return i
		}
	}
	return -1
}
