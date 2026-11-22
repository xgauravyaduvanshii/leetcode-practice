// LeetCode 2035. Partition Array Into Two Arrays to Minimize Sum Difference — Hard
// https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference/
// Submission 2201556187 — Accepted, Go
//
// My thinking: I split the array in half and
// list every subset sum of each half by how
// many numbers it takes, then pair the halves
// so their sums land as close to half the total
// as they can.

package main

import "sort"

func minimumDifference(nums []int) int {
	n := len(nums) / 2
	total := 0
	for _, x := range nums {
		total += x
	}
	subsetSums := func(arr []int) map[int][]int {
		d := map[int][]int{0: {0}}
		for _, x := range arr {
			nd := map[int][]int{}
			for cnt, sums := range d {
				nd[cnt] = append(nd[cnt], sums...)
				taken := make([]int, len(sums))
				for i, s := range sums {
					taken[i] = s + x
				}
				nd[cnt+1] = append(nd[cnt+1], taken...)
			}
			d = nd
		}
		return d
	}
	left := subsetSums(nums[:n])
	right := subsetSums(nums[n:])
	for cnt := range right {
		sort.Ints(right[cnt])
	}
	ans := 1 << 62
	for cnt1, sums1 := range left {
		cnt2 := n - cnt1
		sums2, ok := right[cnt2]
		if !ok {
			continue
		}
		for _, s1 := range sums1 {
			target := total/2 - s1
			idx := sort.Search(len(sums2), func(i int) bool { return sums2[i] >= target })
			for _, j := range []int{idx - 1, idx} {
				if j >= 0 && j < len(sums2) {
					diff := total - 2*(s1+sums2[j])
					if diff < 0 {
						diff = -diff
					}
					if diff < ans {
						ans = diff
					}
				}
			}
		}
	}
	return ans
}
