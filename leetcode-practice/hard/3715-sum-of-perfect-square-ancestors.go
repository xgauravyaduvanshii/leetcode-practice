// LeetCode 3715. Sum of Perfect Square Ancestors — Hard
// https://leetcode.com/problems/sum-of-perfect-square-ancestors/
// Submission 2203060612 — Accepted, Go
//
// My thinking: nums[i] * nums[a] is a perfect square exactly
// when the two numbers have the same squarefree part — the
// product of the primes that occur to an odd power in each
// number, since the even-power primes already form a square
// on their own. So I replace every value by its squarefree
// part, then walk the tree from the root keeping a count of
// the squarefree parts seen on the current root path: every
// ancestor whose part matches the current node's part forms
// a perfect square with it. The count is added when I enter
// a node and removed when I leave it, so it always holds
// just the ancestors, never the siblings or the node itself.
func sumOfAncestors(n int, edges [][]int, nums []int) int64 {
	adj := make([][]int, n)
	for _, e := range edges {
		u, v := e[0], e[1]
		adj[u] = append(adj[u], v)
		adj[v] = append(adj[v], u)
	}

	// Smallest prime factor sieve up to the largest value.
	limit := 0
	for _, x := range nums {
		if x > limit {
			limit = x
		}
	}
	spf := make([]int, limit+1)
	for i := 2; i <= limit; i++ {
		if spf[i] == 0 {
			spf[i] = i
			if i*i <= limit {
				for j := i * i; j <= limit; j += i {
					if spf[j] == 0 {
						spf[j] = i
					}
				}
			}
		}
	}
	spf[1] = 1

	// squarefree strips the primes in pairs — only a prime
	// left over an odd number of times survives.
	squarefree := func(x int) int {
		res := 1
		for x > 1 {
			p := spf[x]
			odd := 0
			for x%p == 0 {
				x /= p
				odd ^= 1
			}
			if odd == 1 {
				res *= p
			}
		}
		return res
	}

	part := make([]int, n)
	for i, x := range nums {
		part[i] = squarefree(x)
	}

	onPath := make(map[int]int)
	ans := 0
	// Iterative DFS with an explicit exit marker, so a
	// 1e5-deep chain never overflows the call stack.
	type frame struct {
		node, parent int
		exiting      bool
	}
	stack := []frame{{node: 0, parent: -1}}
	for len(stack) > 0 {
		f := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		if f.exiting {
			onPath[part[f.node]]--
			continue
		}
		ans += onPath[part[f.node]]
		onPath[part[f.node]]++
		stack = append(stack, frame{node: f.node, parent: f.parent, exiting: true})
		for _, nb := range adj[f.node] {
			if nb != f.parent {
				stack = append(stack, frame{node: nb, parent: f.node})
			}
		}
	}
	return int64(ans)
}
