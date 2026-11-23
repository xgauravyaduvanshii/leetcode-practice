// LeetCode 2603. Collect Coins in a Tree — Hard
// https://leetcode.com/problems/collect-coins-in-a-tree/
// Submission 2201847765 — Accepted, Go
//
// My thinking: a branch with no coin
// is never worth entering, and a coin
// two steps away can be picked up from
// where I stand, so I trim the empty
// branches, then peel two layers off the
// edge — what is left is the road I must
// walk, there and back.

package main

func collectTheCoins(coins []int, edges [][]int) int {
	n := len(coins)
	adj := make([][]int, n)
	deg := make([]int, n)
	for _, e := range edges {
		a, b := e[0], e[1]
		adj[a] = append(adj[a], b)
		adj[b] = append(adj[b], a)
		deg[a]++
		deg[b]++
	}
	removed := make([]bool, n)
	// step 1: trim branches that hold no coin
	queue := []int{}
	for i := 0; i < n; i++ {
		if deg[i] == 1 && coins[i] == 0 {
			queue = append(queue, i)
		}
	}
	for len(queue) > 0 {
		u := queue[0]
		queue = queue[1:]
		removed[u] = true
		for _, w := range adj[u] {
			if !removed[w] {
				deg[w]--
				if deg[w] == 1 && coins[w] == 0 {
					queue = append(queue, w)
				}
			}
		}
	}
	// step 2: peel two layers — coins within distance 2 are collected
	// from the core, so the outer layers need no visit
	for round := 0; round < 2; round++ {
		leaves := []int{}
		for i := 0; i < n; i++ {
			if !removed[i] && deg[i] <= 1 {
				leaves = append(leaves, i)
			}
		}
		if len(leaves) == 0 {
			break
		}
		for _, u := range leaves {
			removed[u] = true
		}
		for _, u := range leaves {
			for _, w := range adj[u] {
				if !removed[w] {
					deg[w]--
				}
			}
		}
	}
	remaining := 0
	for i := 0; i < n; i++ {
		if !removed[i] {
			remaining++
		}
	}
	if remaining <= 1 {
		return 0
	}
	return 2 * (remaining - 1)
}
