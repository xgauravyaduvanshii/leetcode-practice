// LeetCode 3134. Find the Median of the Uniqueness Array — Hard
// https://leetcode.com/problems/find-the-median-of-the-uniqueness-array/
// Submission 2202026185 — Accepted, Go
//
// My thinking: the median uniqueness is
// the smallest x such that at least half
// the subarrays have at most x distinct
// values. I count those subarrays for a
// given x with a sliding window — the
// window's right end only moves forward,
// so each count is linear — and
// binary-search the smallest x that
// reaches half.

func medianOfUniquenessArray(nums []int) int {
    n := len(nums)
    total := n * (n + 1) / 2
    k := (total + 1) / 2
    countLE := func(x int) int {
        cnt := make(map[int]int)
        distinct := 0
        left := 0
        res := 0
        for right, v := range nums {
            if cnt[v] == 0 {
                distinct++
            }
            cnt[v]++
            for distinct > x {
                cnt[nums[left]]--
                if cnt[nums[left]] == 0 {
                    distinct--
                }
                left++
            }
            res += right - left + 1
        }
        return res
    }
    uniq := make(map[int]bool)
    for _, v := range nums {
        uniq[v] = true
    }
    lo, hi := 1, len(uniq)
    for lo < hi {
        mid := (lo + hi) / 2
        if countLE(mid) >= k {
            hi = mid
        } else {
            lo = mid + 1
        }
    }
    return lo
}
