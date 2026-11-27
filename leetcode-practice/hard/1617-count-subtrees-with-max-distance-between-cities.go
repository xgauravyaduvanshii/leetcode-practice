func countSubgraphsForEachDiameter(n int, edges [][]int) []int {
	// My thinking: with at most 15 cities, try every group
	// of them — keep the connected ones and sort them by
	// their widest gap.
	adj := make([][]int, n)
	for _, e := range edges {
		u, v := e[0]-1, e[1]-1
		adj[u] = append(adj[u], v)
		adj[v] = append(adj[v], u)
	}
	ans := make([]int, n-1)
	bfs := func(start int, nodes map[int]bool) map[int]int {
		dist := map[int]int{start: 0}
		queue := []int{start}
		for len(queue) > 0 {
			x := queue[0]
			queue = queue[1:]
			for _, y := range adj[x] {
				if nodes[y] {
					if _, ok := dist[y]; !ok {
						dist[y] = dist[x] + 1
						queue = append(queue, y)
					}
				}
			}
		}
		return dist
	}
	for mask := 1; mask < (1 << n); mask++ {
		nodes := map[int]bool{}
		for i := 0; i < n; i++ {
			if mask>>i&1 == 1 {
				nodes[i] = true
			}
		}
		if len(nodes) < 2 {
			continue
		}
		start := 0
		for v := range nodes {
			start = v
			break
		}
		dist := bfs(start, nodes)
		if len(dist) != len(nodes) {
			continue
		}
		far := start
		for v, d := range dist {
			if d > dist[far] {
				far = v
			}
		}
		dist2 := bfs(far, nodes)
		d := 0
		for _, v := range dist2 {
			if v > d {
				d = v
			}
		}
		ans[d-1]++
	}
	return ans
}
