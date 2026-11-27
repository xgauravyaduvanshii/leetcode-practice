// LeetCode 3821. Find Nth Smallest Integer With K One Bits — Hard
// https://leetcode.com/problems/find-nth-smallest-integer-with-k-one-bits/
// Submission 2203196410 — Accepted, Go
//
// My thinking: decide the answer bit by bit from the top
// (bit 49) down. With i lower bits still free and k ones
// left to place, setting the current bit to 0 leaves
// exactly C(i, k) numbers; if n is larger than that, the
// nth number must have this bit set, so I set it, subtract
// C(i, k) from n and use up one of the k ones. Otherwise
// the bit stays 0. Once all k ones are placed the remaining
// bits are 0, and the guarantee that the answer is below
// 2^50 means 50 bits are always enough. The binomial table
// is built once with Pascal's rule; n is int64 because it
// can be as large as 2^50.
func nthSmallest(n int64, k int) int64 {
	const mx = 50
	var c [mx][mx + 1]int64
	for i := 0; i < mx; i++ {
		c[i][0] = 1
		for j := 1; j <= i; j++ {
			c[i][j] = c[i-1][j-1] + c[i-1][j]
		}
	}
	var ans int64
	for i := 49; i >= 0; i-- {
		if k == 0 {
			break
		}
		if n > c[i][k] {
			n -= c[i][k]
			ans |= int64(1) << i
			k--
		}
	}
	return ans
}
