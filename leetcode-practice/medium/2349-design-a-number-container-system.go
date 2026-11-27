// LeetCode 2349. Design a Number Container System — Medium
// https://leetcode.com/problems/design-a-number-container-system/
// Submission 2204730766 — Accepted, Go
//
// My thinking: same idea as the Python version — an index->number map
// plus a min-heap of indices per number, with stale heap tops lazily
// popped in find() when their index now holds a different number.
import "container/heap"

type IntHeap []int

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *IntHeap) Push(x any)        { *h = append(*h, x.(int)) }
func (h *IntHeap) Pop() any {
    old := *h
    n := len(old)
    x := old[n-1]
    *h = old[:n-1]
    return x
}

type NumberContainers struct {
    indexToNum map[int]int
    numToHeap  map[int]*IntHeap
}

func Constructor() NumberContainers {
    return NumberContainers{
        indexToNum: make(map[int]int),
        numToHeap:  make(map[int]*IntHeap),
    }
}

func (this *NumberContainers) Change(index int, number int) {
    this.indexToNum[index] = number
    h, ok := this.numToHeap[number]
    if !ok {
        h = &IntHeap{}
        heap.Init(h)
        this.numToHeap[number] = h
    }
    heap.Push(h, index)
}

func (this *NumberContainers) Find(number int) int {
    h, ok := this.numToHeap[number]
    if !ok || h.Len() == 0 {
        return -1
    }
    for h.Len() > 0 {
        top := (*h)[0]
        if num, ok := this.indexToNum[top]; ok && num == number {
            return top
        }
        heap.Pop(h)
    }
    return -1
}
