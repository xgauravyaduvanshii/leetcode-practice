// LeetCode 3887. Incremental Even-Weighted Cycle Queries — Hard
// https://leetcode.com/problems/incremental-even-weighted-cycle-queries/
// Submission 2203351106 — Accepted, Go
//
// My thinking: adding an edge creates a new cycle only
// when its ends are already connected, and every other
// cycle keeps its weight, so only the new cycle can break
// the all-even invariant. Its weight is the new edge's
// weight plus the weight of any path between its ends, so
// I need path parities in the graph so far. A union-find
// with xor-to-root keeps exactly that: two vertices are
// connected when they share a root, and the parity
// between them is the xor of their xors to the root. A
// disconnected edge is always added and joins the two
// sets with the xor that makes the edge's weight
// consistent; a connected edge is added exactly when its
// weight matches the existing parity, and then it changes
// nothing, since it is consistent with every path already
// there.
func numberOfEdgesAdded(n int, edges [][]int) int {
	parent := make([]int, n)
	xr := make([]int, n)
	for i := range parent {
		parent[i] = i
	}
	var find func(x int) (int, int)
	find = func(x int) (int, int) {
		if parent[x] == x {
			return x, 0
		}
		path := []int{}
		for parent[x] != x {
			path = append(path, x)
			x = parent[x]
		}
		root := x
		suf := 0
		for i := len(path) - 1; i >= 0; i-- {
			suf ^= xr[path[i]]
			xr[path[i]] = suf
			parent[path[i]] = root
		}
		return root, xr[path[0]]
	}
	ans := 0
	for _, e := range edges {
		u, v, w := e[0], e[1], e[2]
		ru, xu := find(u)
		rv, xv := find(v)
		if ru != rv {
			parent[ru] = rv
			xr[ru] = xu ^ xv ^ w
			ans++
		} else if xu ^ xv == w {
			ans++
		}
	}
	return ans
}
