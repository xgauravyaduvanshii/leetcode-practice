// LeetCode 2735. Collecting Chocolates — Medium
// https://leetcode.com/problems/collecting-chocolates/
// Submission 2205223510 — Accepted, Go
//
// My thinking: same idea as the Python version — after k
// rotations each type costs the cheapest of the k+1 positions
// it has visited; try every k and keep the cheapest total
// including the k*x rotation cost.
func minCost(nums []int, x int) int64 {
    n := len(nums)
    cur := make([]int, n)
    copy(cur, nums)
    var ans int64
    for _, v := range cur {
        ans += int64(v)
    }
    for k := 1; k < n; k++ {
        var total int64 = int64(k * x)
        for i := 0; i < n; i++ {
            if nums[(i-k+n)%n] < cur[i] {
                cur[i] = nums[(i-k+n)%n]
            }
            total += int64(cur[i])
        }
        if total < ans {
            ans = total
        }
    }
    return ans
}
