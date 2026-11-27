// LeetCode 6. Zigzag Conversion — Medium
// https://leetcode.com/problems/zigzag-conversion/
// Submission 2203756374 — Accepted, Go

// My thinking: walk the rows top to bottom and back up, appending each
// character to its row, then join the rows. A single row returns the
// string unchanged.
import "strings"

func convert(s string, numRows int) string {
    if numRows == 1 {
        return s
    }
    rows := make([]strings.Builder, numRows)
    r := 0
    step := 1
    for _, ch := range s {
        rows[r].WriteRune(ch)
        if r == 0 {
            step = 1
        } else if r == numRows-1 {
            step = -1
        }
        r += step
    }
    var sb strings.Builder
    for i := 0; i < numRows; i++ {
        sb.WriteString(rows[i].String())
    }
    return sb.String()
}
