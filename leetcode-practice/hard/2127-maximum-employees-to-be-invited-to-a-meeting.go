// LeetCode 2127. Maximum Employees to Be Invited to a Meeting — Hard
// https://leetcode.com/problems/maximum-employees-to-be-invited-to-a-meeting/
// Submission 2201581920 — Accepted, Go
//
// My thinking: everyone points at a favourite,
// so the picture is rings with chains hanging
// off them — a ring of three or more stands
// alone, but a mutual pair can take the two
// longest chains feeding into it, and all the
// mutual pairs can come at once.

package main

func maximumInvitations(favorite []int) int {
	n := len(favorite)
	indeg := make([]int, n)
	for _, f := range favorite {
		indeg[f]++
	}
	// Peel off the chains; what stays behind is in rings.
	queue := []int{}
	for i := 0; i < n; i++ {
		if indeg[i] == 0 {
			queue = append(queue, i)
		}
	}
	chain := make([]int, n)
	inRing := make([]bool, n)
	for i := range inRing {
		inRing[i] = true
	}
	for len(queue) > 0 {
		u := queue[0]
		queue = queue[1:]
		inRing[u] = false
		v := favorite[u]
		if chain[u]+1 > chain[v] {
			chain[v] = chain[u] + 1
		}
		indeg[v]--
		if indeg[v] == 0 {
			queue = append(queue, v)
		}
	}
	// Every mutual pair plus its two chains can come together.
	pairTotal := 0
	longestRing := 0
	seen := make([]bool, n)
	for i := 0; i < n; i++ {
		if !inRing[i] || seen[i] {
			continue
		}
		ring := []int{}
		u := i
		for !seen[u] {
			seen[u] = true
			ring = append(ring, u)
			u = favorite[u]
		}
		if len(ring) == 2 {
			pairTotal += 2 + chain[ring[0]] + chain[ring[1]]
		} else if len(ring) > longestRing {
			longestRing = len(ring)
		}
	}
	if pairTotal > longestRing {
		return pairTotal
	}
	return longestRing
}
