// LeetCode 1872. Stone Game VIII — Hard
// https://leetcode.com/problems/stone-game-viii/
// Submission 2201212048 — Accepted, TypeScript
//
// My thinking: taking a prefix leaves the other
// player the best value of the game on what is
// left, so I walk the prefix sums from the end —
// at each point I either take everything or take
// this prefix and hand over the best value so
// far.

function stoneGameVIII(stones: number[]): number {
    const prefix: number[] = [];
    let sum = 0;
    for (const v of stones) {
        sum += v;
        prefix.push(sum);
    }
    let res = prefix[prefix.length - 1];
    for (let i = stones.length - 2; i > 0; i--) {
        res = Math.max(res, prefix[i] - res);
    }
    return res;
}
