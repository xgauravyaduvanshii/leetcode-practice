// LeetCode 2766. Relocate Marbles — Medium
// https://leetcode.com/problems/relocate-marbles/
// Submission 2205251435 — Accepted, Go
//
// My thinking: same idea as the Python version — a set of
// occupied positions; each move empties its source and fills
// its destination, then the set is sorted for the answer.
func relocateMarbles(nums []int, moveFrom []int, moveTo []int) []int {
    occupied := map[int]bool{}
    for _, x := range nums {
        occupied[x] = true
    }
    for i := range moveFrom {
        delete(occupied, moveFrom[i])
        occupied[moveTo[i]] = true
    }
    ans := make([]int, 0, len(occupied))
    for x := range occupied {
        ans = append(ans, x)
    }
    sort.Ints(ans)
    return ans
}
