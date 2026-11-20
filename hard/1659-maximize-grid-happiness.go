func getMaxGridHappiness(m int, n int, introvertsCount int, extrovertsCount int) int {
	// My thinking: fill the grid one cell at a time — an
	// introvert starts at 120 and loses 30 per neighbour,
	// an extrovert starts at 40 and gains 20 per neighbour,
	// so a new cell only changes itself and the neighbours
	// above and to its left.
	type key struct {
		idx, intro, extro int
		above, cur [5]int
	}
	memo := map[key]int{}
	var dp func(idx, intro, extro int, above, cur [5]int) int
	dp = func(idx, intro, extro int, above, cur [5]int) int {
		if idx == m*n {
			return 0
		}
		k := key{idx, intro, extro, above, cur}
		if v, ok := memo[k]; ok {
			return v
		}
		i, j := idx/n, idx%n
		var best int
		if j == n-1 {
			best = dp(idx+1, intro, extro, cur, [5]int{}) // leave empty, row ends
		} else {
			best = dp(idx+1, intro, extro, above, cur) // leave empty
		}
		neigh := []int{}
		if i > 0 {
			neigh = append(neigh, above[j])
		}
		if j > 0 {
			neigh = append(neigh, cur[j-1])
		}
		for _, cand := range []struct {
			kind, left, base, own int
		}{{1, intro, 120, -30}, {2, extro, 40, 20}} {
			if cand.left == 0 {
				continue
			}
			gain := cand.base
			for _, nb := range neigh {
				if nb == 0 {
					continue
				}
				gain += cand.own
				if nb == 1 {
					gain -= 30
				} else {
					gain += 20
				}
			}
			newCur := cur
			newCur[j] = cand.kind
			newAbove := above
			if j == n-1 {
				newAbove = newCur
				newCur = [5]int{}
			}
			ni, ne := intro, extro
			if cand.kind == 1 {
				ni--
			} else {
				ne--
			}
			if v := gain + dp(idx+1, ni, ne, newAbove, newCur); v > best {
				best = v
			}
		}
		memo[k] = best
		return best
	}
	return dp(0, introvertsCount, extrovertsCount, [5]int{}, [5]int{})
}
