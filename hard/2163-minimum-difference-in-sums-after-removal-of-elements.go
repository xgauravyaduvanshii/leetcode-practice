// LeetCode 2163. Minimum Difference in Sums After Removal of Elements — Hard
// https://leetcode.com/problems/minimum-difference-in-sums-after-removal-of-elements/
// Submission 2201596508 — Accepted, Go
//
// My thinking: the first half wants the
// smallest numbers it can reach and the second
// half wants the largest, so I sweep the split
// point across the middle — a heap keeps the n
// smallest on the left and the n largest on
// the right, and the best split wins.

package main

import "container/heap"

type IntHeap struct {
	vals []int
	less func(a, b int) bool
}

func (h IntHeap) Len() int { return len(h.vals) }
func (h IntHeap) Less(i, j int) bool { return h.less(h.vals[i], h.vals[j]) }
func (h IntHeap) Swap(i, j int) { h.vals[i], h.vals[j] = h.vals[j], h.vals[i] }
func (h *IntHeap) Push(x any) { h.vals = append(h.vals, x.(int)) }
func (h *IntHeap) Pop() any {
	old := h.vals
	n := len(old)
	x := old[n-1]
	h.vals = old[:n-1]
	return x
}

func minimumDifference(nums []int) int {
	n := len(nums) / 3
	// Smallest-sum of n elements among the first i (i from n to 2n).
	leftSum := make([]int, 2*n+1)
	maxHeap := &IntHeap{less: func(a, b int) bool { return a > b }}
	for _, x := range nums[:n] {
		heap.Push(maxHeap, x)
	}
	total := 0
	for _, x := range nums[:n] {
		total += x
	}
	leftSum[n] = total
	for i := n; i < 2*n; i++ {
		heap.Push(maxHeap, nums[i])
		total += nums[i]
		total -= heap.Pop(maxHeap).(int)
		leftSum[i+1] = total
	}
	// Largest-sum of n elements among the last 3n - i (i from 2n down to n).
	rightSum := make([]int, 2*n+1)
	minHeap := &IntHeap{less: func(a, b int) bool { return a < b }}
	for _, x := range nums[2*n:] {
		heap.Push(minHeap, x)
	}
	total = 0
	for _, x := range nums[2*n:] {
		total += x
	}
	rightSum[2*n] = total
	for i := 2*n - 1; i >= n; i-- {
		heap.Push(minHeap, nums[i])
		total += nums[i]
		total -= heap.Pop(minHeap).(int)
		rightSum[i] = total
	}
	ans := leftSum[n] - rightSum[n]
	for i := n + 1; i <= 2*n; i++ {
		if d := leftSum[i] - rightSum[i]; d < ans {
			ans = d
		}
	}
	return ans
}
