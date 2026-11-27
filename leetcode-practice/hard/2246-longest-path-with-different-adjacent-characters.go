// LeetCode 2246. Longest Path With Different Adjacent Characters — Hard
// https://leetcode.com/problems/longest-path-with-different-adjacent-characters/
// Submission 2201637099 — Accepted, Go
//
// My thinking: the best run through any
// node is its two longest downward runs
// from children wearing a different letter
// — I grow those bottom-up and keep the
// best join I ever see.

package main

func longestPath(parent []int, s string) int {
	n := len(parent)
	children := make([][]int, n)
	for i := 1; i < n; i++ {
		children[parent[i]] = append(children[parent[i]], i)
	}
	ans := 1
	var dfs func(u int) int
	dfs = func(u int) int {
		top1, top2 := 0, 0
		for _, v := range children[u] {
			cur := dfs(v)
			if s[v] != s[u] {
				if cur > top1 {
					top2 = top1
					top1 = cur
				} else if cur > top2 {
					top2 = cur
				}
			}
		}
		if 1+top1+top2 > ans {
			ans = 1 + top1 + top2
		}
		return 1 + top1
	}
	dfs(0)
	return ans
}
