// LeetCode 1815. Maximum Number of Groups Getting Fresh Donuts — Hard
// https://leetcode.com/problems/maximum-number-of-groups-getting-fresh-donuts/
// Submission 2201183148 — Accepted, JavaScript
//
// My thinking: groups with no remainder are always
// fresh, and complementary remainders pair up into
// fresh groups on their own — whatever is left I
// order by trying every next remainder and keeping
// the running total modulo the batch size.

function maxHappyGroups(batchSize, groups) {
    const cnt = new Map();
    for (const g of groups) {
        const r = g % batchSize;
        cnt.set(r, (cnt.get(r) ?? 0) + 1);
    }
    let ans = cnt.get(0) ?? 0;
    cnt.delete(0);
    for (let r = 1; r < batchSize; r++) {
        if ((cnt.get(r) ?? 0) === 0) continue;
        const comp = batchSize - r;
        if (r === comp) {
            ans += Math.floor(cnt.get(r) / 2);
            cnt.set(r, cnt.get(r) % 2);
        } else if (r < comp) {
            const pairs = Math.min(cnt.get(r), cnt.get(comp) ?? 0);
            ans += pairs;
            cnt.set(r, cnt.get(r) - pairs);
            cnt.set(comp, (cnt.get(comp) ?? 0) - pairs);
        }
    }
    const remainders = [];
    for (let r = 1; r < batchSize; r++) {
        if ((cnt.get(r) ?? 0) > 0) remainders.push(r);
    }
    const init = remainders.map(r => cnt.get(r) ?? 0);
    const memo = new Map();
    function dp(state, cur) {
        const key = state.join(",") + "|" + cur;
        if (memo.has(key)) return memo.get(key);
        let best = 0;
        for (let idx = 0; idx < remainders.length; idx++) {
            if (state[idx] === 0) continue;
            const next = state.slice();
            next[idx]--;
            const ncur = (cur + remainders[idx]) % batchSize;
            const gain = ncur === 0 ? 1 : 0;
            best = Math.max(best, gain + dp(next, ncur));
        }
        memo.set(key, best);
        return best;
    }
    return ans + dp(init, 0);
}
