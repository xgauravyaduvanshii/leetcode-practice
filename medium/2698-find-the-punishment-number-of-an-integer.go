// LeetCode 2698. Find the Punishment Number of an Integer — Medium
// https://leetcode.com/problems/find-the-punishment-number-of-an-integer/
// Submission 2205196181 — Accepted, Go
//
// My thinking: same idea as the Python version — depth-first
// over the decimal digits of i*i, trying every first-part
// length and pruning when the remaining sum goes negative; the
// digits are built by hand (itoa) because the LeetCode Go stub
// has no imports.
func punishmentNumber(n int) int {
    itoa := func(v int) string {
        if v == 0 {
            return "0"
        }
        digits := []byte{}
        for v > 0 {
            digits = append([]byte{byte('0' + v%10)}, digits...)
            v /= 10
        }
        return string(digits)
    }
    var can func(s string, target int) bool
    can = func(s string, target int) bool {
        if len(s) == 0 {
            return target == 0
        }
        if target < 0 {
            return false
        }
        for i := 1; i <= len(s); i++ {
            v := 0
            for _, ch := range s[:i] {
                v = v*10 + int(ch-'0')
            }
            if v > target {
                break
            }
            if can(s[i:], target-v) {
                return true
            }
        }
        return false
    }
    ans := 0
    for i := 1; i <= n; i++ {
        if can(itoa(i*i), i) {
            ans += i * i
        }
    }
    return ans
}
