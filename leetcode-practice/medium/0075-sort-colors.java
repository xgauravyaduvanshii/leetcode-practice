// LeetCode 75. Sort Colors — Medium
// https://leetcode.com/problems/sort-colors/
// Submission 2203845497 — Accepted, Java

// My thinking: I keep three regions with three pointers — reds at the
// front, whites in the middle, blues at the back — and scan the middle
// region once. A 0 swaps to the front and both front pointers move, a
// 2 swaps to the back and the back pointer moves in, and a 1 is already
// in place, so I just move on. One pass, no extra space.
class Solution {
    public void sortColors(int[] nums) {
        int low = 0, mid = 0, high = nums.length - 1;
        while (mid <= high) {
            if (nums[mid] == 0) {
                int tmp = nums[low];
                nums[low] = nums[mid];
                nums[mid] = tmp;
                low++;
                mid++;
            } else if (nums[mid] == 2) {
                int tmp = nums[mid];
                nums[mid] = nums[high];
                nums[high] = tmp;
                high--;
            } else {
                mid++;
            }
        }
    }
}
