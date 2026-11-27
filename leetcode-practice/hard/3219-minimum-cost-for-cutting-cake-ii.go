// LeetCode 3219. Minimum Cost for Cutting Cake II — Hard
// https://leetcode.com/problems/minimum-cost-for-cutting-cake-ii/
// Submission 2202100248 — Accepted, Go
//
// My thinking: cutting the more expensive
// line first is always better, because
// its cost is multiplied by fewer pieces.
// I sort both cut lists descending and
// take the larger next cut each time,
// multiplying by how many pieces the
// other direction already has.

func minimumCost(m int, n int, horizontalCut []int, verticalCut []int) int64 {
    sort.Slice(horizontalCut, func(i, j int) bool { return horizontalCut[i] > horizontalCut[j] })
    sort.Slice(verticalCut, func(i, j int) bool { return verticalCut[i] > verticalCut[j] })
    var hPieces int64 = 1
    var vPieces int64 = 1
    i := 0
    j := 0
    var total int64 = 0
    for i < len(horizontalCut) || j < len(verticalCut) {
        if j == len(verticalCut) || (i < len(horizontalCut) && horizontalCut[i] > verticalCut[j]) {
            total += int64(horizontalCut[i]) * vPieces
            hPieces++
            i++
        } else {
            total += int64(verticalCut[j]) * hPieces
            vPieces++
            j++
        }
    }
    return total
}
