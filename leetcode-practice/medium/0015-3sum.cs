// LeetCode 15. 3Sum — Medium
// https://leetcode.com/problems/3sum/
// Submission 2203805934 — Accepted, C#

// My thinking: I sort the numbers, then fix the first element of each
// triplet and find the other two with two pointers moving in from the
// ends. Skipping equal neighbours at every step keeps duplicate
// triplets out, and the sorted order tells me which pointer to move:
// too small a sum, move left up; too big, move right down.
public class Solution {
    public IList<IList<int>> ThreeSum(int[] nums) {
        Array.Sort(nums);
        int n = nums.Length;
        var ans = new List<IList<int>>();
        for (int i = 0; i < n - 2; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            int left = i + 1, right = n - 1;
            while (left < right) {
                int total = nums[i] + nums[left] + nums[right];
                if (total < 0) left++;
                else if (total > 0) right--;
                else {
                    ans.Add(new List<int> { nums[i], nums[left], nums[right] });
                    left++;
                    right--;
                    while (left < right && nums[left] == nums[left - 1]) left++;
                    while (left < right && nums[right] == nums[right + 1]) right--;
                }
            }
        }
        return ans;
    }
}
