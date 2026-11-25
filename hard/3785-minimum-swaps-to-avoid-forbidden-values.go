// LeetCode 3785. Minimum Swaps to Avoid Forbidden Values — Hard
// https://leetcode.com/problems/minimum-swaps-to-avoid-forbidden-values/
// Submission 2203178253 — Accepted, Go
func minSwaps(nums []int, forbidden []int) int {
	// My thinking: the multiset of values never changes, so
	// first check the rearrangement is even possible. All
	// copies of a value v must land on positions that do
	// not forbid v, so we need count(v) <= n - count of
	// positions forbidding v for every v; that one check
	// per value is also enough, because any two different
	// values together can use every position between them.
	// With that settled, look at the bad positions, where
	// nums[i] == forbidden[i]. Swapping two bad positions
	// holding different values fixes both at once, so
	// ceil(bad / 2) swaps suffice unless one value
	// dominates the bad spots: if maxBad copies of the same
	// value are bad, each of the extras beyond the other
	// bad spots needs its own swap with a good position,
	// which costs maxBad swaps. The answer is the larger
	// of the two counts.
	n := len(nums)
	total := make(map[int]int)
	forbids := make(map[int]int)
	for i := 0; i < n; i++ {
		total[nums[i]]++
		forbids[forbidden[i]]++
	}
	for v, c := range total {
		if c > n-forbids[v] {
			return -1
		}
	}
	bad := 0
	badCount := make(map[int]int)
	for i := 0; i < n; i++ {
		if nums[i] == forbidden[i] {
			bad++
			badCount[nums[i]]++
		}
	}
	if bad == 0 {
		return 0
	}
	maxBad := 0
	for _, c := range badCount {
		if c > maxBad {
			maxBad = c
		}
	}
	if (bad+1)/2 > maxBad {
		return (bad + 1) / 2
	}
	return maxBad
}
