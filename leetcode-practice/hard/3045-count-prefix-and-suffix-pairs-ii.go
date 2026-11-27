// LeetCode 3045. Count Prefix and Suffix Pairs II — Hard
// https://leetcode.com/problems/count-prefix-and-suffix-pairs-ii/
// Submission 2201910177 — Accepted, Go
//
// My thinking: a word only pairs with an
// earlier word that is one of its borders
// — a proper head that is also its tail
// — or the word itself. I walk each
// word's borders through its KMP prefix
// links and count how many earlier words
// match each border. Borders are keyed
// by length and a 64-bit rolling hash, so
// looking one up never copies the string.

func countPrefixSuffixPairs(words []string) int {
	const base uint64 = 131
	seen := map[[2]uint64]int{}
	ans := 0
	for _, w := range words {
		n := len(w)
		// Prefix hashes (64-bit overflow arithmetic).
		h := make([]uint64, n+1)
		for i := 0; i < n; i++ {
			h[i+1] = h[i]*base + uint64(w[i])
		}
		// KMP prefix function.
		pi := make([]int, n)
		for i := 1; i < n; i++ {
			j := pi[i-1]
			for j > 0 && w[i] != w[j] {
				j = pi[j-1]
			}
			if w[i] == w[j] {
				j++
			}
			pi[i] = j
		}
		// Every border length, from the whole word down
		// through the KMP links.
		for length := n; length > 0; length = pi[length-1] {
			key := [2]uint64{uint64(length), h[length]}
			ans += seen[key]
		}
		key := [2]uint64{uint64(n), h[n]}
		seen[key]++
	}
	return ans
}
