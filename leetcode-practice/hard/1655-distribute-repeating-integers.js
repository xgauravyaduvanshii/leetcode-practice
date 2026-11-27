/**
 * @param {number[]} nums
 * @param {number[]} quantity
 * @return {boolean}
 */
var canDistribute = function(nums, quantity) {
    // My thinking: the hungriest customer picks first —
    // give them any value with enough copies left, and
    // remember the dead ends so they are not retried.
    const freq = new Map();
    for (const x of nums) freq.set(x, (freq.get(x) || 0) + 1);
    const counts = [...freq.values()].sort((a, b) => b - a);
    quantity = [...quantity].sort((a, b) => b - a);
    const memo = new Map();
    function dfs(qi, state) {
        if (qi === quantity.length) return true;
        const key = qi + '|' + state.join(',');
        if (memo.has(key)) return memo.get(key);
        const q = quantity[qi];
        const seen = new Set();
        for (let i = 0; i < state.length; i++) {
            const c = state[i];
            if (c < q || seen.has(c)) continue;
            seen.add(c);
            const ns = [...state];
            ns[i] -= q;
            ns.sort((a, b) => b - a);
            if (dfs(qi + 1, ns)) { memo.set(key, true); return true; }
        }
        memo.set(key, false);
        return false;
    }
    return dfs(0, counts);
};
