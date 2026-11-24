// LeetCode 3357. Minimize the Maximum Adjacent Element Difference — Hard
// https://leetcode.com/problems/minimize-the-maximum-adjacent-element-difference/
// Submission 2202423269 -- Accepted, Go
package main

func minDifference(nums []int) int {
	// My thinking: binary-search the answer. For a candidate m, the only
	// pair worth trying is x = mn + m and y = mx - m, where mn/mx are the
	// smallest/largest known values next to a -1: x is the largest value
	// still within m of mn, y the smallest within m of mx, so any gap a
	// feasible pair could fill, this pair fills too. Each gap is then
	// checked on its own: a length-1 gap takes x or y, a longer gap takes
	// all x, all y, x-then-y or y-then-x, and an edge gap takes whichever
	// of x, y is nearer its known neighbour. Adjacent known values bound
	// the search from below.
	n := len(nums)
	allMissing := true
	for _, v := range nums {
		if v != -1 {
			allMissing = false
			break
		}
	}
	if allMissing {
		return 0
	}
	maxGap := 0
	mn := 1000000001
	mx := -1
	hasMissing := false
	for i := 0; i < n; i++ {
		if nums[i] == -1 {
			hasMissing = true
		}
		if i > 0 {
			a, b := nums[i-1], nums[i]
			if a != -1 && b != -1 {
				if d := abs(a - b); d > maxGap {
					maxGap = d
				}
			} else if a == -1 && b != -1 {
				if b < mn {
					mn = b
				}
				if b > mx {
					mx = b
				}
			} else if a != -1 && b == -1 {
				if a < mn {
					mn = a
				}
				if a > mx {
					mx = a
				}
			}
		}
	}
	if !hasMissing {
		return maxGap
	}
	check := func(m, x, y int) bool {
		i := 0
		for i < n {
			if nums[i] != -1 {
				i++
				continue
			}
			j := i
			for j < n && nums[j] == -1 {
				j++
			}
			left, hasLeft := -1, false
			if i > 0 {
				left, hasLeft = nums[i-1], true
			}
			right, hasRight := -1, false
			if j < n {
				right, hasRight = nums[j], true
			}
			switch {
			case !hasLeft && !hasRight:
			case !hasLeft:
				if min(abs(right-x), abs(right-y)) > m {
					return false
				}
			case !hasRight:
				if min(abs(left-x), abs(left-y)) > m {
					return false
				}
			case j-i == 1:
				if min(max(abs(left-x), abs(right-x)), max(abs(left-y), abs(right-y))) > m {
					return false
				}
			default:
				if min(max(abs(left-x), abs(x-right)),
					max(abs(left-y), abs(y-right)),
					max(abs(left-x), abs(x-y), abs(y-right)),
					max(abs(left-y), abs(y-x), abs(x-right))) > m {
					return false
				}
			}
			i = j
		}
		return true
	}
	lo, hi := maxGap, (mx-mn+1)/2
	for lo < hi {
		mid := (lo + hi) / 2
		if check(mid, mn+mid, mx-mid) {
			hi = mid
		} else {
			lo = mid + 1
		}
	}
	return lo
}

func abs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}

func min(a ...int) int {
	m := a[0]
	for _, v := range a[1:] {
		if v < m {
			m = v
		}
	}
	return m
}

func max(a ...int) int {
	m := a[0]
	for _, v := range a[1:] {
		if v > m {
			m = v
		}
	}
	return m
}
