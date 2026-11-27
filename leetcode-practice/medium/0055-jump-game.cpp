// LeetCode 55. Jump Game — Medium
// https://leetcode.com/problems/jump-game/
// Submission 2203830621 — Accepted, C++

// My thinking: I walk the array once, tracking the farthest index I
// can reach from everything seen so far. If I ever arrive at an index
// beyond that reach, the end is unreachable; if the reach covers the
// last index, I can make it. I never need to remember which jumps I
// took, only how far I can get.
class Solution {
public:
    bool canJump(vector<int>& nums) {
        int reach = 0;
        for (int i = 0; i < (int)nums.size(); i++) {
            if (i > reach) return false;
            reach = max(reach, i + nums[i]);
            if (reach >= (int)nums.size() - 1) return true;
        }
        return true;
    }
};
