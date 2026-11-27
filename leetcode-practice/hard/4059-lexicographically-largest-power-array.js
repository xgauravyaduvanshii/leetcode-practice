// LeetCode 4059. Lexicographically Largest Power Array — Hard
// https://leetcode.com/problems/lexicographically-largest-power-array/
// Submission 2203583307 — Accepted, JavaScript
//
// My thinking: work the bits from high (14) to low
// (0), since power[0] matters first, then power[1],
// and so on. Keep the numbers in ordered groups: the
// groups are the blocks of the permutation fixed by
// the higher bits, and inside a group the numbers
// can still be reordered freely without changing any
// power value already decided. For the current bit,
// walk the groups in order and put the numbers that
// have the bit first inside each group, which is the
// longest leading run of set bits this bit can get.
// The moment a group has a number without the bit,
// the run stops there, so split that group into its
// with-bit part (in the run) and its without-bit part
// (right after it) — and leave every later group
// completely alone, because their order no longer
// affects this bit and splitting them would only
// steal freedom from the lower bits. A group whose
// numbers all have the bit just joins the run whole.

var largestPower = function(nums) {
    let groups = [nums.slice()];
    const ans = new Array(15).fill(0);
    for (let b = 14; b >= 0; b--) {
        const newGroups = [];
        let broken = false;
        let prefix = 0;
        for (const g of groups) {
            if (broken) {
                newGroups.push(g);
                continue;
            }
            const withBit = [];
            const without = [];
            for (const x of g) {
                if ((x >> b) & 1) withBit.push(x);
                else without.push(x);
            }
            if (withBit.length === 0) {
                newGroups.push(g);
                broken = true;
            } else if (without.length === 0) {
                newGroups.push(g);
                prefix += g.length;
            } else {
                newGroups.push(withBit);
                newGroups.push(without);
                prefix += withBit.length;
                broken = true;
            }
        }
        groups = newGroups;
        ans[14 - b] = prefix;
    }
    return ans;
};
