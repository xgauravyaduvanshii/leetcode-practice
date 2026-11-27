// LeetCode 18. 4Sum — Medium
// https://leetcode.com/problems/4sum/
// Submission 2203808539 — Accepted, Java

// My thinking: like 3Sum, I sort first and fix the first two numbers
// of each quadruplet, then find the last two with two pointers. I skip
// equal neighbours at both fixed positions and at both pointers, so no
// quadruplet is ever reported twice, and the sorted order tells me
// which pointer to move based on whether the sum is too small or big.
import java.util.*;

class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        Arrays.sort(nums);
        int n = nums.length;
        List<List<Integer>> ans = new ArrayList<>();
        for (int i = 0; i < n - 3; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            for (int j = i + 1; j < n - 2; j++) {
                if (j > i + 1 && nums[j] == nums[j - 1]) continue;
                int left = j + 1, right = n - 1;
                while (left < right) {
                    long total = (long) nums[i] + nums[j] + nums[left] + nums[right];
                    if (total < target) left++;
                    else if (total > target) right--;
                    else {
                        ans.add(Arrays.asList(nums[i], nums[j], nums[left], nums[right]));
                        left++;
                        right--;
                        while (left < right && nums[left] == nums[left - 1]) left++;
                        while (left < right && nums[right] == nums[right + 1]) right--;
                    }
                }
            }
        }
        return ans;
    }
}
