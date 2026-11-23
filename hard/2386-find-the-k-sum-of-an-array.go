// LeetCode 2386. Find the K-Sum of an Array — Hard
// https://leetcode.com/problems/find-the-k-sum-of-an-array/
// Submission 2201712987 — Accepted, Go
//
// My thinking: the biggest sum takes every
// positive number, and every smaller sum
// is that total minus some loss — I grow
// the smallest losses with a heap and
// subtract the (k - 1)-th one. No visited
// set: two different subsequences can
// share one sum and index, and both count.

package main

import (
	"container/heap"
	"sort"
)

type pair2386 struct {
	sum int64
	idx int
}

type minHeap2386 []pair2386

func (h minHeap2386) Len() int            { return len(h) }
func (h minHeap2386) Less(i, j int) bool  { return h[i].sum < h[j].sum }
func (h minHeap2386) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }
func (h *minHeap2386) Push(x interface{}) { *h = append(*h, x.(pair2386)) }
func (h *minHeap2386) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func kSum(nums []int, k int) int64 {
	var total int64
	vals := make([]int64, 0, len(nums))
	for _, x := range nums {
		if x > 0 {
			total += int64(x)
		}
		v := int64(x)
		if v < 0 {
			v = -v
		}
		vals = append(vals, v)
	}
	if k == 1 {
		return total
	}
	sort.Slice(vals, func(i, j int) bool { return vals[i] < vals[j] })
	h := &minHeap2386{{vals[0], 0}}
	heap.Init(h)
	var loss int64
	for t := 0; t < k-1; t++ {
		p := heap.Pop(h).(pair2386)
		loss = p.sum
		i := p.idx
		if i+1 < len(vals) {
			heap.Push(h, pair2386{loss + vals[i+1], i + 1})
			heap.Push(h, pair2386{loss - vals[i] + vals[i+1], i + 1})
		}
	}
	return total - loss
}
