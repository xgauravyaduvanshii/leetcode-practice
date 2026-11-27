// LeetCode 2281. Sum of Total Strength of Wizards — Hard
// https://leetcode.com/problems/sum-of-total-strength-of-wizards/
// Submission 2201655001 — Accepted, Go
//
// My thinking: every subarray has one
// weakest wizard, so I hand each wizard the
// stretches where it is the weakest and
// add its strength times every subarray
// sum those stretches hold.

package main

const mod2281 = 1000000007

func totalStrength(strength []int) int {
	n := len(strength)
	pref := make([]int, n+1)
	for i, x := range strength {
		pref[i+1] = (pref[i] + x) % mod2281
	}
	prefPref := make([]int, n+2)
	for i := 0; i <= n; i++ {
		prefPref[i+1] = (prefPref[i] + pref[i]) % mod2281
	}
	left := make([]int, n)
	stack := []int{}
	for i, x := range strength {
		for len(stack) > 0 && strength[stack[len(stack)-1]] >= x {
			stack = stack[:len(stack)-1]
		}
		if len(stack) == 0 {
			left[i] = -1
		} else {
			left[i] = stack[len(stack)-1]
		}
		stack = append(stack, i)
	}
	right := make([]int, n)
	stack = []int{}
	for i := n - 1; i >= 0; i-- {
		x := strength[i]
		for len(stack) > 0 && strength[stack[len(stack)-1]] > x {
			stack = stack[:len(stack)-1]
		}
		if len(stack) == 0 {
			right[i] = n
		} else {
			right[i] = stack[len(stack)-1]
		}
		stack = append(stack, i)
	}
	ans := 0
	for i, x := range strength {
		L := left[i] + 1
		R := right[i] - 1
		leftCount := i - L + 1
		rightCount := R - i + 1
		sumRight := (prefPref[R+2] - prefPref[i+1]) % mod2281
		if sumRight < 0 {
			sumRight += mod2281
		}
		sumLeft := (prefPref[i+1] - prefPref[L]) % mod2281
		if sumLeft < 0 {
			sumLeft += mod2281
		}
		subSum := (leftCount*sumRight - rightCount*sumLeft) % mod2281
		if subSum < 0 {
			subSum += mod2281
		}
		ans = (ans + x*subSum) % mod2281
	}
	return ans
}
