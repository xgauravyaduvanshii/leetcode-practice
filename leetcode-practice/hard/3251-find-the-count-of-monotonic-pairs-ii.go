// LeetCode 3251. Find the Count of Monotonic Pairs II — Hard
// https://leetcode.com/problems/find-the-count-of-monotonic-pairs-ii/
// Submission 2202142576 — Accepted, Go
//
// My thinking: split each nums[i] into arr1[i]
// + arr2[i] with arr1 non-decreasing and arr2
// non-increasing. I keep a DP over the value of
// arr1[i]; moving to the next number, arr1 must
// grow by at least max(0, nums[i] - nums[i-1])
// to keep arr2 non-increasing, and a prefix sum
// makes each transition O(1).

func countOfPairs(nums []int) int {
    const MOD = 1000000007
    dp := make([]int, nums[0]+1)
    for i := range dp {
        dp[i] = 1
    }
    for i := 1; i < len(nums); i++ {
        d := nums[i] - nums[i-1]
        need := 0
        if d > 0 {
            need = d
        }
        pref := make([]int, len(dp)+1)
        for t := 0; t < len(dp); t++ {
            pref[t+1] = (pref[t] + dp[t]) % MOD
        }
        ndp := make([]int, nums[i]+1)
        for s := 0; s <= nums[i]; s++ {
            lim := s - need
            if lim >= 0 {
                if lim >= len(dp) {
                    lim = len(dp) - 1
                }
                ndp[s] = pref[lim+1]
            }
        }
        dp = ndp
    }
    ans := 0
    for _, v := range dp {
        ans = (ans + v) % MOD
    }
    return ans
}
