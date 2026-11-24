// LeetCode 3533. Concatenated Divisibility — Hard
// https://leetcode.com/problems/concatenated-divisibility/
// Submission 2202812620 — Accepted, TypeScript
function concatenatedDivisibility(nums: number[], k: number): number[] {
    // My thinking: appending a number x with d digits multiplies
    // the running remainder by 10^d and adds x, all modulo k.
    // Whether the remaining numbers can finish the job depends
    // only on which numbers are left and the current remainder,
    // so I memoise that feasibility check over (subset, remainder)
    // and then build the answer greedily: at each position take
    // the smallest unused number that still leaves a feasible
    // completion. If none exists at all, the answer is empty.
    const n = nums.length;
    const pow10: number[] = nums.map((v) => {
        let p = 1;
        for (let i = 0; i < String(v).length; i++) p = (p * 10) % k;
        return p;
    });
    const memo = new Map<string, boolean>();
    function feasible(mask: number, r: number): boolean {
        if (mask === 0) return r === 0;
        const key = mask + "," + r;
        const hit = memo.get(key);
        if (hit !== undefined) return hit;
        for (let i = 0; i < n; i++) {
            if ((mask >> i) & 1) {
                if (feasible(mask ^ (1 << i), (r * pow10[i] + nums[i]) % k)) {
                    memo.set(key, true);
                    return true;
                }
            }
        }
        memo.set(key, false);
        return false;
    }
    if (!feasible((1 << n) - 1, 0)) return [];
    const res: number[] = [];
    let mask = (1 << n) - 1;
    let r = 0;
    const order = nums.map((_, i) => i).sort((a, b) => nums[a] - nums[b] || a - b);
    for (let t = 0; t < n; t++) {
        for (const i of order) {
            if (!((mask >> i) & 1)) continue;
            const nr = (r * pow10[i] + nums[i]) % k;
            if (feasible(mask ^ (1 << i), nr)) {
                res.push(nums[i]);
                mask ^= 1 << i;
                r = nr;
                break;
            }
        }
    }
    return res;
}
