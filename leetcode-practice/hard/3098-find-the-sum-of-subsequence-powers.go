// LeetCode 3098. Find the Sum of Subsequence Powers — Hard
// https://leetcode.com/problems/find-the-sum-of-subsequence-powers/
// Submission 2201990815 — Accepted, Go
//
// My thinking: after sorting, a
// subsequence's power is the smallest
// gap between consecutive elements. For
// a candidate gap d I count the
// subsequences of size k whose gaps are
// all at least d, with a DP over the
// sorted numbers. Counting this for
// every distinct gap and adding
// (d - previous d) times the count gives
// the sum over all subsequences.

func sumOfPowers(nums []int, k int) int {
    const MOD int64 = 1000000007
    n := len(nums)
    for i := 0; i < n; i++ {
        for j := i + 1; j < n; j++ {
            if nums[j] < nums[i] {
                nums[i], nums[j] = nums[j], nums[i]
            }
        }
    }
    diffSet := map[int]bool{}
    for i := 0; i < n; i++ {
        for j := i + 1; j < n; j++ {
            d := nums[j] - nums[i]
            if d > 0 {
                diffSet[d] = true
            }
        }
    }
    if len(diffSet) == 0 {
        return 0
    }
    diffs := make([]int, 0, len(diffSet))
    for d := range diffSet {
        diffs = append(diffs, d)
    }
    for i := 0; i < len(diffs); i++ {
        for j := i + 1; j < len(diffs); j++ {
            if diffs[j] < diffs[i] {
                diffs[i], diffs[j] = diffs[j], diffs[i]
            }
        }
    }
    countGe := func(d int) int64 {
        limits := make([]int, n)
        for i := 0; i < n; i++ {
            lim := -1
            for j := i - 1; j >= 0; j-- {
                if nums[j] <= nums[i]-d {
                    lim = j
                    break
                }
            }
            limits[i] = lim
        }
        dp := make([]int64, n)
        for i := range dp {
            dp[i] = 1
        }
        for length := 2; length <= k; length++ {
            pref := make([]int64, n)
            var s int64
            for i, v := range dp {
                s = (s + v) % MOD
                pref[i] = s
            }
            ndp := make([]int64, n)
            any := false
            for i := 0; i < n; i++ {
                if limits[i] >= 0 {
                    ndp[i] = pref[limits[i]]
                    if ndp[i] != 0 {
                        any = true
                    }
                }
            }
            dp = ndp
            if !any {
                return 0
            }
        }
        var total int64
        for _, v := range dp {
            total = (total + v) % MOD
        }
        return total
    }
    var ans int64
    prev := 0
    for _, d := range diffs {
        c := countGe(d)
        if c != 0 {
            ans = (ans + int64(d-prev)*c) % MOD
        }
        prev = d
    }
    return int(ans)
}
