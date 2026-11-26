// LeetCode 81. Search in Rotated Sorted Array II — Medium
// https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
// Submission 2203958669 — Accepted, Rust
//
// My thinking:
// The array is sorted but rotated, and it may contain duplicates.
// A plain binary search still works most of the time: compare nums[mid]
// with nums[left] to tell which half is sorted, then check whether the
// target lies inside that sorted half and shrink the window accordingly.
// The only trouble is duplicates: when nums[left] == nums[mid] == nums[right],
// we cannot tell which half is sorted, so we shrink both ends by one and
// try again. In the worst case (all duplicates) that is linear, but it is
// correct and fast on typical inputs.

impl Solution {
    pub fn search(nums: Vec<i32>, target: i32) -> bool {
        let mut left: i32 = 0;
        let mut right: i32 = nums.len() as i32 - 1;

        while left <= right {
            let mid = (left + right) / 2;
            if nums[mid as usize] == target {
                return true;
            }

            // Duplicates hide which half is sorted: shrink both ends.
            if nums[left as usize] == nums[mid as usize]
                && nums[mid as usize] == nums[right as usize]
            {
                left += 1;
                right -= 1;
            }
            // Left half is sorted.
            else if nums[left as usize] <= nums[mid as usize] {
                if nums[left as usize] <= target && target < nums[mid as usize] {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            }
            // Right half is sorted.
            else {
                if nums[mid as usize] < target && target <= nums[right as usize] {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
        }

        false
    }
}
