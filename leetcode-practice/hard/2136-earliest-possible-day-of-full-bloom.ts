// LeetCode 2136. Earliest Possible Day of Full Bloom — Hard
// https://leetcode.com/problems/earliest-possible-day-of-full-bloom/
// Submission 2201585490 — Accepted, TypeScript
//
// My thinking: while one seed is in the ground
// the others are still being planted, so the
// seed that takes longest to grow should go in
// first — plant in order of longest grow time
// and the last bloom is the answer.

function earliestFullBloom(plantTime: number[], growTime: number[]): number {
    const order = plantTime.map((_, i) => i).sort((a, b) => growTime[b] - growTime[a]);
    let day = 0;
    let ans = 0;
    for (const i of order) {
        day += plantTime[i];
        ans = Math.max(ans, day + growTime[i]);
    }
    return ans;
}
