// LeetCode 4064. Longest Subarray Divisible by K with At Most One Negation II — Hard
// https://leetcode.com/problems/longest-subarray-divisible-by-k-with-at-most-one-negation-ii/
// Submission 2203590863 — Accepted, Go
//
// My thinking: a subarray nums[l..r] has sum S, and
// negating one element nums[t] inside it changes the
// sum to S - 2*nums[t]. So it is valid when S is
// already 0 mod k, or when some t inside it has
// 2*nums[t] equal to S mod k. With prefix remainders
// P, the sum of nums[l..r] is P[r+1] - P[l] mod k,
// so for remainders a = P[l] and b = P[r+1] the
// negation needs a t with 2*nums[t] equal to b - a
// mod k, sitting between l and r. For fixed
// remainders a and b, the longest such subarray uses
// the earliest l with remainder a and the latest
// r+1 with remainder b — any narrower choice is
// shorter, and if no doubled residue lands inside
// that widest window, none lands inside a narrower
// one either. So I take the first and last
// occurrence of every remainder, then for each
// doubled residue d check every pair (a, b = a+d):
// the pair is good when the first position of d at
// or after first[a] still lies before last[b], which
// is a binary search over the sorted positions of
// d. The no-negation case is the same idea with
// a = b. That is O(n + k^2) work.

import "sort"

func longestSubarray(nums []int, k int) int {
	n := len(nums)
	pref := make([]int, n+1)
	for i, x := range nums {
		r := (pref[i] + x) % k
		if r < 0 {
			r += k
		}
		pref[i+1] = r
	}
	first := make([]int, k)
	last := make([]int, k)
	for r := range first {
		first[r] = -1
		last[r] = -1
	}
	for i, r := range pref {
		if first[r] < 0 {
			first[r] = i
		}
		last[r] = i
	}
	ans := 0
	for r := 0; r < k; r++ {
		if first[r] >= 0 && last[r]-first[r] > ans {
			ans = last[r] - first[r]
		}
	}
	pos := make([][]int, k)
	for t, x := range nums {
		d := (2 * x) % k
		if d < 0 {
			d += k
		}
		pos[d] = append(pos[d], t)
	}
	for d := 0; d < k; d++ {
		p := pos[d]
		if len(p) == 0 {
			continue
		}
		for a := 0; a < k; a++ {
			if first[a] < 0 {
				continue
			}
			b := (a + d) % k
			if last[b] < 0 {
				continue
			}
			j := sort.SearchInts(p, first[a])
			if j < len(p) && p[j] < last[b] && last[b]-first[a] > ans {
				ans = last[b] - first[a]
			}
		}
	}
	return ans
}
