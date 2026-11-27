func frogPosition(n int, edges [][]int, t int, target int) float64 {
	// My thinking: the frog picks uniformly among the
	// neighbours it has not visited — so walk the tree
	// spreading the probability, and stop the moment the
	// clock runs out or the frog gets stuck.
	graph := make([][]int, n+1)
	for _, e := range edges {
		graph[e[0]] = append(graph[e[0]], e[1])
		graph[e[1]] = append(graph[e[1]], e[0])
	}
	type state struct {
		node int
		prob float64
		time int
	}
	queue := []state{{1, 1.0, 0}}
	seen := map[int]bool{1: true}
	for len(queue) > 0 {
		cur := queue[0]
		queue = queue[1:]
		if cur.node == target {
			if cur.time == t {
				return cur.prob
			}
			unvisited := 0
			for _, nb := range graph[cur.node] {
				if !seen[nb] {
					unvisited++
				}
			}
			if unvisited == 0 {
				return cur.prob
			}
			return 0.0
		}
		if cur.time == t {
			continue
		}
		var unvisited []int
		for _, nb := range graph[cur.node] {
			if !seen[nb] {
				unvisited = append(unvisited, nb)
			}
		}
		if len(unvisited) == 0 {
			continue
		}
		for _, nb := range unvisited {
			seen[nb] = true
			queue = append(queue, state{nb, cur.prob / float64(len(unvisited)), cur.time + 1})
		}
	}
	return 0.0
}
