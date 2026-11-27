// LeetCode 1968. Array With Elements Not Equal to Average of Neighbors — Medium
// https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/
// Submission 2204263332 — Accepted, Java

// My thinking: an element is safe when it is not the average of its
// two neighbours, which is guaranteed if it sits strictly above both
// of them or strictly below both of them. So I sort the numbers,
// split them into a smaller half and a larger half, and weave the
// halves together large-small-large-small: every small element then
// sits between two larger ones, and every large element between two
// smaller ones, so no element can be the average of its neighbours.
// When the array is odd the smaller half has one extra element, and
// it goes at the end, where it has only one neighbour and needs no
// check at all.
import java.util.Arrays;

class Solution {
    public int[] rearrangeArray(int[] nums) {
        Arrays.sort(nums);
        int n = nums.length;
        int mid = (n + 1) / 2;
        int[] out = new int[n];
        int o = 0;
        for (int i = 0; i < n - mid; i++) {
            out[o++] = nums[mid + i];
            out[o++] = nums[i];
        }
        if (mid > n - mid) {
            out[o] = nums[mid - 1];
        }
        return out;
    }
}
