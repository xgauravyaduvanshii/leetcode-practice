func maxSum(nums1 []int, nums2 []int) int {
	// My thinking: walk both sorted lists together — at
	// every shared number you may switch, so take the
	// richer of the two stretches since the last switch.
	const MOD = 1000000007
	i, j := 0, 0
	sum1, sum2, total := 0, 0, 0
	n, m := len(nums1), len(nums2)
	for i < n && j < m {
		if nums1[i] < nums2[j] {
			sum1 += nums1[i]
			i++
		} else if nums1[i] > nums2[j] {
			sum2 += nums2[j]
			j++
		} else {
			if sum1 > sum2 {
				total += sum1
			} else {
				total += sum2
			}
			total += nums1[i]
			i++
			j++
			sum1, sum2 = 0, 0
		}
	}
	for i < n {
		sum1 += nums1[i]
		i++
	}
	for j < m {
		sum2 += nums2[j]
		j++
	}
	if sum1 > sum2 {
		total += sum1
	} else {
		total += sum2
	}
	return total % MOD
}
