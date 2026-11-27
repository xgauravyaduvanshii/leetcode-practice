func findMaxValueOfEquation(points [][]int, k int) int {
	// My thinking: with x already sorted, the value splits
	// into (y - x) from the left point plus (y + x) from
	// the right — so keep a sliding window of the best
	// left halves within reach.
	best := -1 << 60
	type pair struct{ x, v int }
	window := []pair{}
	for _, p := range points {
		x, y := p[0], p[1]
		for len(window) > 0 && x-window[0].x > k {
			window = window[1:]
		}
		if len(window) > 0 {
			if cand := window[0].v + y + x; cand > best {
				best = cand
			}
		}
		value := y - x
		for len(window) > 0 && window[len(window)-1].v <= value {
			window = window[:len(window)-1]
		}
		window = append(window, pair{x, value})
	}
	return best
}
