// LeetCode 2294. Partition Array Such That Maximum Difference Is K — Medium
// https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/
// Submission 2204656019 — Accepted, Go
//
// My thinking: same idea as the Python version — sort, then greedily
// start a new group whenever a number is more than k away from the
// current group's first number.
func partitionArray(nums []int, k int) int {
    sort.Ints(nums)
    ans := 1
    start := nums[0]
    for _, x := range nums[1:] {
        if x-start > k {
            ans++
            start = x
        }
    }
    return ans
}
