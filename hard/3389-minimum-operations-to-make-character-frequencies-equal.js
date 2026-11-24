// LeetCode 3389. Minimum Operations to Make Character Frequencies Equal — Hard
// https://leetcode.com/problems/minimum-operations-to-make-character-frequencies-equal/
// Submission 2202500932 — Accepted 773/773, JavaScript
//
// My thinking: pick the target frequency every kept letter ends up with,
// then walk the alphabet left to right. Letters only ever change forward,
// so surplus characters are carried to the next letter at one operation a
// step, which beats deleting one here and inserting one there (two
// operations). At each letter I either keep it at the target, paying to
// drop the surplus or fill the shortfall, or drop it to zero, paying for
// all its characters; either way the carried surplus can be anything up to
// the target, so I keep the cheapest cost per carry and take a suffix
// minimum over it. The last letter cannot carry anything past 'z'.

/**
 * @param {string} s
 * @return {number}
 */
var makeStringGood = function(s) {
    const cnt = new Array(26).fill(0);
    for (const ch of s) cnt[ch.charCodeAt(0) - 97]++;
    let best = s.length;
    const mx = Math.max(...cnt);
    for (let target = 1; target <= mx; target++) {
        let dp = new Array(target + 1).fill(Infinity);
        dp[0] = 0;
        for (let i = 0; i < 26; i++) {
            const c = cnt[i];
            const last = i === 25;
            const bestAt = new Array(target + 2).fill(Infinity);
            for (let carry = 0; carry <= target; carry++) {
                if (dp[carry] === Infinity) continue;
                const avail = c + carry;
                if (avail >= target) {
                    const v = dp[carry] + avail - target;
                    const u = last ? 0 : Math.min(avail - target, target);
                    if (v < bestAt[u]) bestAt[u] = v;
                } else {
                    const v = dp[carry] + target - avail;
                    if (v < bestAt[0]) bestAt[0] = v;
                }
                const v = dp[carry] + avail;
                const u = last ? 0 : Math.min(avail, target);
                if (v < bestAt[u]) bestAt[u] = v;
            }
            const ndp = new Array(target + 1).fill(Infinity);
            let suf = Infinity;
            for (let j = target; j >= 0; j--) {
                if (bestAt[j] < suf) suf = bestAt[j];
                ndp[j] = suf;
            }
            dp = ndp;
        }
        best = Math.min(best, dp[0]);
    }
    return best;
};
