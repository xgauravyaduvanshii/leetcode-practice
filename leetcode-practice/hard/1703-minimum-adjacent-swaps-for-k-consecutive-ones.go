// LeetCode 1703. Minimum Adjacent Swaps for K Consecutive Ones — Hard
// https://leetcode.com/problems/minimum-adjacent-swaps-for-k-consecutive-ones/
// Submission 2201101470 — Accepted, Go
//
// My thinking: only the ones matter, so I list their
// positions and slide a window of k across them — for
// each window I count how far every one has to travel
// to sit next to the middle one, using prefix sums to
// keep it fast.

func minMoves(nums []int, k int) int {
    ones := []int{}
    for i, v := range nums {
        if v == 1 {
            ones = append(ones, i)
        }
    }
    q := make([]int, len(ones))
    for i, pos := range ones {
        q[i] = pos - i
    }
    prefix := make([]int, len(q)+1)
    for i, v := range q {
        prefix[i+1] = prefix[i] + v
    }
    best := 1 << 60
    for i := 0; i+k <= len(q); i++ {
        mid := i + k/2
        median := q[mid]
        left := median*(mid-i) - (prefix[mid] - prefix[i])
        right := (prefix[i+k] - prefix[mid+1]) - median*(i+k-mid-1)
        if left+right < best {
            best = left + right
        }
    }
    return best
}
