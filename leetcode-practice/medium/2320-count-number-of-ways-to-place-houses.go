// LeetCode 2320. Count Number of Ways to Place Houses — Medium
// https://leetcode.com/problems/count-number-of-ways-to-place-houses/
// Submission 2204687257 — Accepted, Go
//
// My thinking: same idea as the Python version — one side of the street
// is a Fibonacci count built iteratively, and the two independent sides
// make the answer that count squared, modulo 10^9+7.
func countHousePlacements(n int) int {
    const MOD = 1000000007
    a, b := 1, 2
    for i := 0; i < n-1; i++ {
        a, b = b, (a+b)%MOD
    }
    return b * b % MOD
}
