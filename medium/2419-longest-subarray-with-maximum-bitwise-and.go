// LeetCode 2419. Longest Subarray With Maximum Bitwise AND — Medium
// https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/
// Submission 2204859700 — Accepted, Go
//
// My thinking: same idea as the Python version — the maximum AND is
// max(nums), so the answer is the longest run of that value.
func longestSubarray(nums []int) int {
    target := nums[0]
    for _, x := range nums {
        if x > target {
            target = x
        }
    }
    best, cur := 0, 0
    for _, x := range nums {
        if x == target {
            cur++
        } else {
            cur = 0
        }
        if cur > best {
            best = cur
        }
    }
    return best
}
