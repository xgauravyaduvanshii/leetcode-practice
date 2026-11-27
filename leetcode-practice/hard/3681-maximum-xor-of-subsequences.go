// LeetCode 3681. Maximum XOR of Subsequences — Hard
// https://leetcode.com/problems/maximum-xor-of-subsequences/
// Submission 2203038540 — Accepted, Go
func maxXorSubsequences(nums []int) int {
	// My thinking: XOR-ing the two subsequences cancels any
	// element picked twice, so X XOR Y is just the XOR of
	// some subset of nums — and every subset is reachable
	// (put it in the first subsequence, leave the second
	// empty). So the answer is the largest XOR any subset
	// can give, which a binary linear basis finds greedily:
	// keep one basis vector per highest bit, then build the
	// answer bit by bit from the top, taking a vector
	// whenever it makes the answer bigger.
	var basis [31]int
	for _, x := range nums {
		v := x
		for b := 30; b >= 0; b-- {
			if v>>b&1 == 0 {
				continue
			}
			if basis[b] == 0 {
				basis[b] = v
				break
			}
			v ^= basis[b]
		}
	}
	ans := 0
	for b := 30; b >= 0; b-- {
		if ans^basis[b] > ans {
			ans ^= basis[b]
		}
	}
	return ans
}
