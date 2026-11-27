// LeetCode 2274. Maximum Consecutive Floors Without Special Floors — Medium
// https://leetcode.com/problems/maximum-consecutive-floors-without-special-floors/
// Submission 2204621545 — Accepted, Go
//
// My thinking: same idea as the Python version — sort the special floors,
// collect the free stretches (bottom edge to first special, between
// neighbours, last special to top edge) and return the longest one.
func maxConsecutive(bottom int, top int, special []int) int {
    sort.Ints(special)
    gaps := []int{special[0] - bottom, top - special[len(special)-1]}
    for i := 1; i < len(special); i++ {
        gaps = append(gaps, special[i]-special[i-1]-1)
    }
    sort.Ints(gaps)
    return gaps[len(gaps) - 1]
}
