// LeetCode 2279. Maximum Bags With Full Capacity of Rocks — Medium
// https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/
// Submission 2204627971 — Accepted, TypeScript
//
// My thinking: same idea as the Python version — each bag needs capacity
// minus rocks more rocks; sort those needs ascending and fill the
// cheapest bags first with the extra rocks, since every full bag counts
// the same.
function maximumBags(capacity: number[], rocks: number[], additionalRocks: number): number {
    const needs = capacity.map((c, i) => c - rocks[i]).sort((a, b) => a - b);
    let ans = 0;
    for (const need of needs) {
        if (additionalRocks >= need) {
            additionalRocks -= need;
            ans++;
        } else {
            break;
        }
    }
    return ans;
};
