// LeetCode 3753. Total Waviness of Numbers in Range II — Hard
// https://leetcode.com/problems/total-waviness-of-numbers-in-range-ii/
// Submission 2203155824 — Accepted, Go
import "strconv"

func totalWaviness(num1 int64, num2 int64) int64 {
	// My thinking: the waviness of one number is the count
	// of its interior digits that are peaks or valleys, so
	// I count it with a digit DP: walking the decimal
	// digits left to right I only need the previous two
	// digits to tell whether the middle one is a peak or a
	// valley, plus the tight flag and whether any non-zero
	// digit has started yet (leading zeros are not digits
	// of the number). The DP returns both how many numbers
	// a prefix admits and their total waviness, and the
	// answer for [num1, num2] is the prefix total at num2
	// minus the prefix total at num1 - 1.
	return totalUpTo(num2) - totalUpTo(num1-1)
}

func totalUpTo(n int64) int64 {
	if n <= 0 {
		return 0
	}
	digits := []int{}
	for _, c := range strconv.FormatInt(n, 10) {
		digits = append(digits, int(c-'0'))
	}
	var memo [17][11][11][2][2]int64
	var seen [17][11][11][2]bool
	var dfs func(i, prev2, prev1 int, tight, started bool) (int64, int64)
	dfs = func(i, prev2, prev1 int, tight, started bool) (int64, int64) {
		if i == len(digits) {
			return 1, 0
		}
		si := 0
		if started {
			si = 1
		}
		if !tight && seen[i][prev2+1][prev1+1][si] {
			m := memo[i][prev2+1][prev1+1][si]
			return m[0], m[1]
		}
		limit := 9
		if tight {
			limit = digits[i]
		}
		var count, wav int64
		for d := 0; d <= limit; d++ {
			ntight := tight && d == limit
			nstarted := started || d != 0
			if !nstarted {
				c, w := dfs(i+1, -1, -1, ntight, false)
				count += c
				wav += w
				continue
			}
			var add int64
			if started && prev2 != -1 {
				if (prev1 > prev2 && prev1 > d) || (prev1 < prev2 && prev1 < d) {
					add = 1
				}
			}
			nprev2, nprev1 := -1, d
			if started {
				nprev2, nprev1 = prev1, d
			}
			c, w := dfs(i+1, nprev2, nprev1, ntight, true)
			count += c
			wav += w + add*c
		}
		if !tight {
			seen[i][prev2+1][prev1+1][si] = true
			memo[i][prev2+1][prev1+1][si] = [2]int64{count, wav}
		}
		return count, wav
	}
	_, w := dfs(0, -1, -1, true, false)
	return w
}
