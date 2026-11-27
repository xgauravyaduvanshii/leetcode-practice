// LeetCode 3395. Subsequences with a Unique Middle Mode I — Hard
// https://leetcode.com/problems/subsequences-with-a-unique-middle-mode-i/
// Submission 2202504375 — Accepted 947/947, Go
package main

func subsequencesWithMiddleMode(nums []int) int {
	// My thinking: fix the middle index. Its value v is the unique mode
	// exactly when it occurs more often than any other value in the five
	// chosen spots. With x of the four other spots equal to v the middle
	// value occurs 1 + x times, so x = 0 can never work, x >= 2 always
	// works, and x = 1 works only when the three remaining values are all
	// different from each other. I count the x >= 2 choices by subtracting
	// the x = 0 and x = 1 choices from all choices, and the x = 1 choices
	// with distinct others by counting pairs on the far side whose two
	// values differ and neither equals the near side's value.
	const mod = 1000000007
	c2 := func(n int) int {
		if n < 2 {
			return 0
		}
		return n * (n - 1) / 2
	}
	n := len(nums)
	before := map[int]int{}
	after := map[int]int{}
	for _, v := range nums {
		after[v]++
	}
	ans := 0
	for m := 0; m < n; m++ {
		v := nums[m]
		after[v]--
		if after[v] == 0 {
			delete(after, v)
		}
		left, right := m, n-1-m
		if left >= 2 && right >= 2 {
			lv := before[v]
			rv := after[v]
			sb := left - lv
			sa := right - rv
			total := c2(left) * c2(right)
			xy0 := c2(sb) * c2(sa)
			xy1 := lv*sb*c2(sa) + c2(sb)*rv*sa
			ge2 := total - xy0 - xy1
			da := c2(sa)
			for w, c := range after {
				if w != v {
					da -= c2(c)
				}
			}
			db := c2(sb)
			for w, c := range before {
				if w != v {
					db -= c2(c)
				}
			}
			sA := 0
			for w, cbw := range before {
				if w == v {
					continue
				}
				caw := after[w]
				sA += cbw * (da - caw*(sa-caw))
			}
			sB := 0
			for w, caw := range after {
				if w == v {
					continue
				}
				cbw := before[w]
				sB += caw * (db - cbw*(sb-cbw))
			}
			ans = (ans + ge2 + lv*sA + rv*sB) % mod
		}
		before[v]++
	}
	return ans
}
