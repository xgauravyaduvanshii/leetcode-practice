// LeetCode 3426. Manhattan Distances of All Arrangements of Pieces — Hard
// https://leetcode.com/problems/manhattan-distances-of-all-arrangements-of-pieces/
// Submission 2202525407 — Accepted 919/919, Go
//
// My thinking: every pair of cells shows up together in
// exactly C(m*n - 2, k - 2) arrangements, so I only need
// the Manhattan distance summed over all cell pairs.
// Rows and columns split apart: the row gaps over all
// pairs are n^2 * C(m+1, 3) and the column gaps are
// m^2 * C(n+1, 3), then I multiply by the pair count,
// all modulo 1e9+7.
func manhattanDistances(m int, n int, k int) int {
	const MOD = 1000000007
	total := m * n
	fact := make([]int64, total+1)
	fact[0] = 1
	for i := 1; i <= total; i++ {
		fact[i] = fact[i-1] * int64(i) % MOD
	}
	modPow := func(a, e int64) int64 {
		res := int64(1)
		a %= MOD
		for e > 0 {
			if e&1 == 1 {
				res = res * a % MOD
			}
			a = a * a % MOD
			e >>= 1
		}
		return res
	}
	invFact := make([]int64, total+1)
	invFact[total] = modPow(fact[total], MOD-2)
	for i := total; i > 0; i-- {
		invFact[i-1] = invFact[i] * int64(i) % MOD
	}
	comb := func(nn, kk int) int64 {
		if kk < 0 || kk > nn {
			return 0
		}
		return fact[nn] * invFact[kk] % MOD * invFact[nn-kk] % MOD
	}
	// C(x+1, 3) = (x+1) * x * (x-1) / 6
	rowSum := int64(m+1) * int64(m) * int64(m-1) / 6
	colSum := int64(n+1) * int64(n) * int64(n-1) / 6
	pairSum := (int64(n)*int64(n)%MOD*rowSum%MOD + int64(m)*int64(m)%MOD*colSum%MOD) % MOD
	return int(comb(total-2, k-2) * pairSum % MOD)
}
