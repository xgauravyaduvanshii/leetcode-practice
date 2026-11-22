// LeetCode 1819. Number of Different Subsequences GCDs — Hard
// https://leetcode.com/problems/number-of-different-subsequences-gcds/
// Submission 2201184052 — Accepted, Go
//
// My thinking: a gcd g is reachable exactly when
// the numbers that are multiples of g have gcd g
// themselves, so I check every g up to the largest
// number.

func countDifferentSubsequenceGCDs(nums []int) int {
    present := make(map[int]bool)
    mx := 0
    for _, v := range nums {
        present[v] = true
        if v > mx {
            mx = v
        }
    }
    ans := 0
    for g := 1; g <= mx; g++ {
        cur := 0
        for m := g; m <= mx; m += g {
            if present[m] {
                cur = gcd(cur, m)
                if cur == g {
                    break
                }
            }
        }
        if cur == g {
            ans++
        }
    }
    return ans
}

func gcd(a, b int) int {
    for b != 0 {
        a, b = b, a%b
    }
    return a
}
