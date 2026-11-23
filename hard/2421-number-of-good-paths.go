// LeetCode 2421. Number of Good Paths — Hard
// https://leetcode.com/problems/number-of-good-paths/
// Submission 2201728582 — Accepted, Go
//
// My thinking: a good path never climbs
// above its endpoints' value, so I wake
// the nodes up from the smallest value
// upward, joining each to its waking
// neighbours — when a value's nodes wake,
// the ones already joined in one piece
// make that many good pairs.

package main

import "sort"

func find2421(parent []int, x int) int {
	for parent[x] != x {
		parent[x] = parent[parent[x]]
		x = parent[x]
	}
	return x
}

func numberOfGoodPaths(vals []int, edges [][]int) int {
	n := len(vals)
	adj := make([][]int, n)
	for _, e := range edges {
		a, b := e[0], e[1]
		adj[a] = append(adj[a], b)
		adj[b] = append(adj[b], a)
	}
	parent := make([]int, n)
	for i := range parent {
		parent[i] = i
	}
	byVal := map[int][]int{}
	for i, v := range vals {
		byVal[v] = append(byVal[v], i)
	}
	keys := make([]int, 0, len(byVal))
	for v := range byVal {
		keys = append(keys, v)
	}
	sort.Ints(keys)
	active := make([]bool, n)
	ans := n
	for _, v := range keys {
		for _, u := range byVal[v] {
			active[u] = true
			for _, w := range adj[u] {
				if active[w] {
					ru, rw := find2421(parent, u), find2421(parent, w)
					if ru != rw {
						parent[rw] = ru
					}
				}
			}
		}
		groups := map[int]int{}
		for _, u := range byVal[v] {
			groups[find2421(parent, u)]++
		}
		for _, cnt := range groups {
			ans += cnt * (cnt - 1) / 2
		}
	}
	return ans
}
