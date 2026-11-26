// LeetCode 3957. Maximum Sum of M Non-Overlapping Subarrays II — Hard
// https://leetcode.com/problems/maximum-sum-of-m-non-overlapping-subarrays-ii/
// Submission 2203473912 — Accepted, Go

func maximumSum(nums []int, m int, l int, r int) int64 {
	// My thinking: let F(k) be the best sum using exactly k
	// subarrays. F is concave in k (each extra subarray can
	// only add less than the one before), so the Aliens trick
	// applies: charge a penalty lam per subarray and solve
	// the unconstrained problem — one linear DP where a
	// subarray ending at i is pref[i] plus the best of
	// dp[j] - pref[j] over j in [i-r, i-l], kept by a
	// monotone deque, with ties broken towards fewer
	// subarrays. If the best single subarray is negative,
	// every F(k) is negative and decreasing, so it is the
	// answer. Otherwise, if the penalty-free optimum already
	// uses at most m subarrays, it is the answer. If not, F
	// is still increasing on [1, m], so the answer is F(m):
	// binary-search the smallest lam whose optimum uses at
	// most m subarrays — at that lam, m is Lagrangian
	// optimal, so the value plus lam * m is exactly F(m).
	n := len(nums)
	pref := make([]int64, n+1)
	for i, x := range nums {
		pref[i+1] = pref[i] + int64(x)
	}
	const NEG int64 = -1 << 60
	wqs := func(lam int64) (int64, int) {
		dp := make([]int64, n+1)
		cnt := make([]int, n+1)
		dq := make([]int, 0, n+1)
		for i := 1; i <= n; i++ {
			j := i - l
			if j >= 0 {
				val := dp[j] - pref[j]
				for len(dq) > 0 {
					bj := dq[len(dq)-1]
					bv := dp[bj] - pref[bj]
					if bv < val || (bv == val && cnt[bj] > cnt[j]) {
						dq = dq[:len(dq)-1]
					} else {
						break
					}
				}
				dq = append(dq, j)
			}
			for len(dq) > 0 && dq[0] < i-r {
				dq = dq[1:]
			}
			dp[i] = dp[i-1]
			cnt[i] = cnt[i-1]
			if len(dq) > 0 {
				bj := dq[0]
				cand := pref[i] + (dp[bj] - pref[bj]) - lam
				cc := cnt[bj] + 1
				if cand > dp[i] || (cand == dp[i] && cc < cnt[i]) {
					dp[i] = cand
					cnt[i] = cc
				}
			}
		}
		return dp[n], cnt[n]
	}
	// Best single subarray (F(1)): same deque DP with k = 1.
	best1 := NEG
	{
		dpPrev := make([]int64, n+1)
		dpCur := make([]int64, n+1)
		for i := range dpCur {
			dpCur[i] = NEG
		}
		dq := make([]int, 0, n+1)
		for i := 1; i <= n; i++ {
			j := i - l
			if j >= 0 {
				val := dpPrev[j] - pref[j]
				for len(dq) > 0 && dpPrev[dq[len(dq)-1]]-pref[dq[len(dq)-1]] <= val {
					dq = dq[:len(dq)-1]
				}
				dq = append(dq, j)
			}
			for len(dq) > 0 && dq[0] < i-r {
				dq = dq[1:]
			}
			if len(dq) > 0 {
				dpCur[i] = pref[i] + (dpPrev[dq[0]] - pref[dq[0]])
			}
			if dpCur[i-1] > dpCur[i] {
				dpCur[i] = dpCur[i-1]
			}
		}
		best1 = dpCur[n]
	}
	if best1 < 0 {
		return best1
	}
	val0, c0 := wqs(0)
	if c0 <= m {
		return val0
	}
	var lo, hi int64 = -100000000000, 100000000000
	for lo < hi {
		mid := lo + (hi-lo)/2
		_, c := wqs(mid)
		if c <= m {
			hi = mid
		} else {
			lo = mid + 1
		}
	}
	val, _ := wqs(lo)
	return val + lo*int64(m)
}
