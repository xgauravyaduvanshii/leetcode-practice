// LeetCode 153. Find Minimum in Rotated Sorted Array — Medium
// https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
// Submission 2204052805 — Accepted, C++

// My thinking: the array was sorted ascending and then rotated, so
// the smallest element is the one place where the order drops — the
// pivot. I binary search for it: at each step I compare the middle
// element with the rightmost one. If nums[mid] is bigger than
// nums[right], the pivot must be to the right of mid, so I move left
// to mid + 1. Otherwise the minimum is at mid or to its left, so I
// move right to mid. When the window closes to one element, that
// element is the minimum. If the array was never rotated, the loop
// still ends at the first element, which is correct.
class Solution {
public:
    int findMin(vector<int>& nums) {
        int left = 0, right = (int)nums.size() - 1;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] > nums[right]) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return nums[left];
    }
};
