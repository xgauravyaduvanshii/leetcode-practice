// LeetCode 46. Permutations — Medium
// https://leetcode.com/problems/permutations/
// Submission 2203825264 — Accepted, C#

// My thinking: I build each permutation one slot at a time with
// backtracking, trying every number I have not used yet in the current
// slot and marking it used until I backtrack. When every slot is
// filled, the current arrangement is one complete permutation.
public class Solution {
    public IList<IList<int>> Permute(int[] nums) {
        var ans = new List<IList<int>>();
        var current = new List<int>();
        var used = new bool[nums.Length];
        Backtrack(nums, used, current, ans);
        return ans;
    }

    private void Backtrack(int[] nums, bool[] used, List<int> current, List<IList<int>> ans) {
        if (current.Count == nums.Length) {
            ans.Add(new List<int>(current));
            return;
        }
        for (int i = 0; i < nums.Length; i++) {
            if (used[i]) continue;
            used[i] = true;
            current.Add(nums[i]);
            Backtrack(nums, used, current, ans);
            current.RemoveAt(current.Count - 1);
            used[i] = false;
        }
    }
}
