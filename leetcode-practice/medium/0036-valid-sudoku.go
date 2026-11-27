// LeetCode 36. Valid Sudoku — Medium
// https://leetcode.com/problems/valid-sudoku/
// Submission 2203818754 — Accepted, Go

// My thinking: I walk every filled cell once and remember which digits
// I have already seen in its row, its column, and its 3x3 box. If a
// digit turns up twice in any of those three groups, the board is
// invalid; if I finish the walk without a repeat, it is valid. The box
// index comes from the row and column divided by 3.
func isValidSudoku(board [][]byte) bool {
    var rows, cols, boxes [9][9]bool
    for r := 0; r < 9; r++ {
        for c := 0; c < 9; c++ {
            ch := board[r][c]
            if ch == '.' {
                continue
            }
            d := ch - '1'
            box := (r/3)*3 + c/3
            if rows[r][d] || cols[c][d] || boxes[box][d] {
                return false
            }
            rows[r][d] = true
            cols[c][d] = true
            boxes[box][d] = true
        }
    }
    return true
}
