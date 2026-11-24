// 3303. Find the Occurrence of First Almost Equal Substring (Hard)
// https://leetcode.com/problems/find-the-occurrence-of-first-almost-equal-substring/
// Submission 2202314109 -- Accepted, Go
package main

func minStartingIndex(s string, pattern string) int {
	// My thinking: a start i works when s[i:i+m] matches pattern in all but
	// at most one position. I find the longest matching prefix of pattern
	// at i with a Z-function on pattern + '#' + s, and the longest matching
	// suffix with a Z-function on the reversed strings. If the prefix match
	// plus the suffix match covers at least m - 1 positions, the uncovered
	// middle is at most one character, so the start is valid. I scan starts
	// from the left and return the first valid one.
	n, m := len(s), len(pattern)

	zFunction := func(t string) []int {
		z := make([]int, len(t))
		left, right := 0, 0
		for i := 1; i < len(t); i++ {
			if i <= right {
				if z[i-left] < right-i+1 {
					z[i] = z[i-left]
				} else {
					z[i] = right - i + 1
				}
			}
			for i+z[i] < len(t) && t[z[i]] == t[i+z[i]] {
				z[i]++
			}
			if i+z[i]-1 > right {
				left, right = i, i+z[i]-1
			}
		}
		return z
	}
	reverse := func(t string) string {
		b := []byte(t)
		for i, j := 0, len(b)-1; i < j; i, j = i+1, j-1 {
			b[i], b[j] = b[j], b[i]
		}
		return string(b)
	}

	zForward := zFunction(pattern + "#" + s)
	zReverse := zFunction(reverse(pattern) + "#" + reverse(s))
	for i := 0; i <= n-m; i++ {
		prefix := zForward[m+1+i]
		if prefix > m {
			prefix = m
		}
		// The suffix of s[i:i+m], reversed, starts at n - (i + m) in s reversed.
		suffix := zReverse[m+1+n-(i+m)]
		if suffix > m {
			suffix = m
		}
		if prefix+suffix >= m-1 {
			return i
		}
	}
	return -1
}
