// LeetCode 3855. Sum of K-Digit Numbers in a Range — Hard
// https://leetcode.com/problems/sum-of-k-digit-numbers-in-a-range/
// Submission 2203297587 — Accepted, Go
//
// My thinking: every position of the k-digit number
// contributes independently. A digit d appears in one
// fixed position in exactly m^(k-1) of the numbers,
// where m = r - l + 1 is how many digits are allowed,
// so a single position contributes (l + ... + r) *
// m^(k-1), and the positions are weighted 1, 10, ...,
// 10^(k-1), a geometric series summing to (10^k - 1)
// / 9. The whole sum is therefore S * m^(k-1) *
// (10^k - 1) / 9 modulo 1e9 + 7, with the division
// done by the modular inverse of 9 and the powers by
// fast exponentiation, which also handles k up to 1e9.
// All products stay below 1e18, so int64 is safe.
func sumOfNumbers(l int, r int, k int) int {
	const mod int64 = 1000000007
	m := int64(r-l+1)
	digitSum := int64(l+r) * m / 2
	geo := (modPow(10, int64(k), mod) - 1 + mod) % mod * modPow(9, mod-2, mod) % mod
	ans := digitSum % mod * modPow(m, int64(k)-1, mod) % mod * geo % mod
	return int(ans)
}

func modPow(base, exp, mod int64) int64 {
	res := int64(1)
	base %= mod
	for exp > 0 {
		if exp&1 == 1 {
			res = res * base % mod
		}
		base = base * base % mod
		exp >>= 1
	}
	return res
}
