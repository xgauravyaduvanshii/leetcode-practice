func maxNumEdgesToRemove(n int, edges [][]int) int {
	// My thinking: shared roads help both, so lay those
	// first — then add each person's own roads only where
	// they still need a connection, and drop the rest.
	parentA := make([]int, n+1)
	parentB := make([]int, n+1)
	for i := 0; i <= n; i++ {
		parentA[i] = i
		parentB[i] = i
	}
	find := func(parent []int, x int) int {
		for parent[x] != x {
			parent[x] = parent[parent[x]]
			x = parent[x]
		}
		return x
	}
	union := func(parent []int, x, y int) bool {
		rx, ry := find(parent, x), find(parent, y)
		if rx == ry {
			return false
		}
		parent[rx] = ry
		return true
	}
	used := 0
	for _, e := range edges {
		if e[0] == 3 {
			a := union(parentA, e[1], e[2])
			b := union(parentB, e[1], e[2])
			if a || b {
				used++
			}
		}
	}
	for _, e := range edges {
		if e[0] == 1 && union(parentA, e[1], e[2]) {
			used++
		}
	}
	for _, e := range edges {
		if e[0] == 2 && union(parentB, e[1], e[2]) {
			used++
		}
	}
	compsA := map[int]bool{}
	compsB := map[int]bool{}
	for i := 1; i <= n; i++ {
		compsA[find(parentA, i)] = true
		compsB[find(parentB, i)] = true
	}
	if len(compsA) != 1 || len(compsB) != 1 {
		return -1
	}
	return len(edges) - used
}
