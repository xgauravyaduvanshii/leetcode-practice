// LeetCode 3585. Find Weighted Median Node in Tree — Hard
// https://leetcode.com/problems/find-weighted-median-node-in-tree/
// Submission 2202862879 — Accepted, Go
package main

func findMedian(n int, edges [][]int, queries [][]int) []int {
	// My thinking: the median is the first node on the path
	// from u whose distance from u reaches half the total path
	// weight. I work with doubled distances so I never touch a
	// float. If the climb to the lowest common ancestor already
	// reaches half, I lift up from u as far as I can while
	// staying under half and take one more step; otherwise the
	// median is on the way down, and I lift up from v as far as
	// the remaining budget allows, which lands on it directly.
	adj := make([][][2]int, n)
	for _, e := range edges {
		u, v, w := e[0], e[1], e[2]
		adj[u] = append(adj[u], [2]int{v, w})
		adj[v] = append(adj[v], [2]int{u, w})
	}
	const LOG = 18
	up := make([][]int, LOG)
	wsum := make([][]int, LOG)
	for k := range up {
		up[k] = make([]int, n)
		wsum[k] = make([]int, n)
		for i := range up[k] {
			up[k][i] = -1
		}
	}
	depth := make([]int, n)
	dist := make([]int, n)
	parent := make([]int, n)
	for i := range parent {
		parent[i] = -1
	}
	order := []int{0}
	parent[0] = -2
	for i := 0; i < len(order); i++ {
		u := order[i]
		for _, vw := range adj[u] {
			v, w := vw[0], vw[1]
			if parent[v] == -1 {
				parent[v] = u
				depth[v] = depth[u] + 1
				dist[v] = dist[u] + w
				up[0][v] = u
				wsum[0][v] = w
				order = append(order, v)
			}
		}
	}
	up[0][0] = 0
	for k := 1; k < LOG; k++ {
		for i := 0; i < n; i++ {
			up[k][i] = up[k-1][up[k-1][i]]
			wsum[k][i] = wsum[k-1][i] + wsum[k-1][up[k-1][i]]
		}
	}
	lca := func(u, v int) int {
		if depth[u] < depth[v] {
			u, v = v, u
		}
		diff := depth[u] - depth[v]
		bit := 0
		for diff > 0 {
			if diff&1 == 1 {
				u = up[bit][u]
			}
			diff >>= 1
			bit++
		}
		if u == v {
			return u
		}
		for k := LOG - 1; k >= 0; k-- {
			if up[k][u] != up[k][v] {
				u = up[k][u]
				v = up[k][v]
			}
		}
		return up[0][u]
	}
	jumpUpLt := func(cur, limit2 int) int {
		acc := 0
		for k := LOG - 1; k >= 0; k-- {
			anc := up[k][cur]
			if anc != -1 && 2*(acc+wsum[k][cur]) < limit2 {
				acc += wsum[k][cur]
				cur = anc
			}
		}
		return cur
	}
	jumpUpLe := func(cur, limit2 int) int {
		acc := 0
		for k := LOG - 1; k >= 0; k-- {
			anc := up[k][cur]
			if anc != -1 && 2*(acc+wsum[k][cur]) <= limit2 {
				acc += wsum[k][cur]
				cur = anc
			}
		}
		return cur
	}
	ans := make([]int, len(queries))
	for qi, q := range queries {
		u, v := q[0], q[1]
		if u == v {
			ans[qi] = u
			continue
		}
		w := lca(u, v)
		du := dist[u] - dist[w]
		dv := dist[v] - dist[w]
		W := du + dv
		if 2*du >= W {
			cur := jumpUpLt(u, W)
			ans[qi] = up[0][cur]
		} else {
			limit2 := 2*dv - W + 2*du
			ans[qi] = jumpUpLe(v, limit2)
		}
	}
	return ans
}
