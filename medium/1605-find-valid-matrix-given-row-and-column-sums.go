// LeetCode 1605. Find Valid Matrix Given Row and Column Sums — Medium
// https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/
// Submission 2204082322 — Accepted, Go

// My thinking: I walk the matrix cell by cell, top to bottom and left
// to right. At each cell I write down the smaller of what its row still
// needs and what its column still needs, then I subtract that amount
// from both remaining sums. Taking the smaller one is safe: whichever
// sum runs out first, its whole row or column is already finished, and
// the other sum still has later cells to fill. Since the row sums and
// column sums add up to the same total, every row and column ends up
// exactly filled when I reach the last cell.
func restoreMatrix(rowSum []int, colSum []int) [][]int {
    rows, cols := len(rowSum), len(colSum)
    matrix := make([][]int, rows)
    for i := range matrix {
        matrix[i] = make([]int, cols)
    }
    for i := 0; i < rows; i++ {
        for j := 0; j < cols; j++ {
            value := rowSum[i]
            if colSum[j] < value {
                value = colSum[j]
            }
            matrix[i][j] = value
            rowSum[i] -= value
            colSum[j] -= value
        }
    }
    return matrix
}
