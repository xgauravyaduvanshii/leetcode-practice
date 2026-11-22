// LeetCode 1862. Sum of Floored Pairs — Hard
// https://leetcode.com/problems/sum-of-floored-pairs/
// Submission 2201207190 — Accepted, Go
//
// My thinking: for each value used as a divisor
// I walk its multiples and count how many numbers
// fall in each quotient band — every such number
// pairs with every copy of the divisor at that
// quotient.

const MOD = 1000000007

func sumOfFlooredPairs(nums []int) int {
    mx := 0
    for _, v := range nums {
        if v > mx {
            mx = v
        }
    }
    cnt := make([]int, mx+1)
    for _, v := range nums {
        cnt[v]++
    }
    pref := make([]int, mx+2)
    for i := 1; i <= mx; i++ {
        pref[i] = pref[i-1] + cnt[i]
    }
    ans := 0
    for d := 1; d <= mx; d++ {
        if cnt[d] == 0 {
            continue
        }
        for mult := d; mult <= mx; mult += d {
            hi := mult + d - 1
            if hi > mx {
                hi = mx
            }
            c := pref[hi] - pref[mult-1]
            ans = (ans + (mult/d)*c*cnt[d]) % MOD
        }
    }
    return ans
}
