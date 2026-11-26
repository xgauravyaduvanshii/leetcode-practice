// LeetCode 59. Spiral Matrix II — Medium
// https://leetcode.com/problems/spiral-matrix-ii/
// Submission 2203835275 — Accepted, Go

// My thinking: I fill the square layer by layer, walking each layer
// in four straight runs — left to right across the top, top to bottom
// down the right side, right to left across the bottom, and bottom to
// top up the left side — writing the next number at each step. After a
// layer is done I shrink the borders by one and start the next layer.
func generateMatrix(n int) [][]int {
    matrix := make([][]int, n)
    for i := range matrix {
        matrix[i] = make([]int, n)
    }
    num := 1
    top, bottom := 0, n-1
    left, right := 0, n-1
    for top <= bottom && left <= right {
        for c := left; c <= right; c++ {
            matrix[top][c] = num
            num++
        }
        top++
        for r := top; r <= bottom; r++ {
            matrix[r][right] = num
            num++
        }
        right--
        for c := right; c >= left; c-- {
            matrix[bottom][c] = num
            num++
        }
        bottom--
        for r := bottom; r >= top; r-- {
            matrix[r][left] = num
            num++
        }
        left++
    }
    return matrix
}
