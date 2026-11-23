// LeetCode 2088. Count Fertile Pyramids in a Land — Hard
// https://leetcode.com/problems/count-fertile-pyramids-in-a-land/
// Submission 2201568381 — Accepted, Go
//
// My thinking: a pyramid stands on the three
// pyramids below it, so I grow the tallest
// pyramid at every cell from the ones under it
// — once pointing down, once pointing up — and
// every extra level above the first is one more
// pyramid.

package main

func countPyramids(grid [][]int) int {
	m := len(grid)
	n := len(grid[0])
	ans := 0
	// f[i][j]: tallest pyramid with apex at (i, j), widening downward.
	f := make([][]int, m)
	for i := range f {
		f[i] = make([]int, n)
	}
	for i := m - 1; i >= 0; i-- {
		for j := 0; j < n; j++ {
			if grid[i][j] == 0 {
				continue
			}
			if i == m-1 || j == 0 || j == n-1 {
				f[i][j] = 1
			} else {
				best := f[i+1][j-1]
				if f[i+1][j] < best {
					best = f[i+1][j]
				}
				if f[i+1][j+1] < best {
					best = f[i+1][j+1]
				}
				f[i][j] = 1 + best
			}
			ans += f[i][j] - 1
		}
	}
	// g[i][j]: tallest pyramid with apex at (i, j), widening upward.
	g := make([][]int, m)
	for i := range g {
		g[i] = make([]int, n)
	}
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j] == 0 {
				continue
			}
			if i == 0 || j == 0 || j == n-1 {
				g[i][j] = 1
			} else {
				best := g[i-1][j-1]
				if g[i-1][j] < best {
					best = g[i-1][j]
				}
				if g[i-1][j+1] < best {
					best = g[i-1][j+1]
				}
				g[i][j] = 1 + best
			}
			ans += g[i][j] - 1
		}
	}
	return ans
}
