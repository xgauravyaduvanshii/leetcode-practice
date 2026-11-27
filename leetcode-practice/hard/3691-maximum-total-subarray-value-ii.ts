// LeetCode 3691. Maximum Total Subarray Value II — Hard
// https://leetcode.com/problems/maximum-total-subarray-value-ii/
// Submission 2203044069 — Accepted, TypeScript
function countGe(nums: number[], t: number): number {
    // My thinking: for a fixed right end, max - min only grows
    // as the left end moves left, so the left ends with value
    // >= t form a prefix [0..left-1]. A sliding window with
    // monotone deques finds that prefix for every right end in
    // linear time, and the prefix lengths add up to the count.
    const n = nums.length;
    const maxd: number[] = [];
    const mind: number[] = [];
    let maxHead = 0;
    let minHead = 0;
    let left = 0;
    let total = 0;
    for (let r = 0; r < n; r++) {
        while (maxd.length > maxHead && nums[maxd[maxd.length - 1]] <= nums[r]) maxd.pop();
        maxd.push(r);
        while (mind.length > minHead && nums[mind[mind.length - 1]] >= nums[r]) mind.pop();
        mind.push(r);
        while (left <= r && nums[maxd[maxHead]] - nums[mind[minHead]] >= t) {
            left++;
            while (maxd[maxHead] < left) maxHead++;
            while (mind[minHead] < left) minHead++;
        }
        total += left;
    }
    return total;
}

function thresholds(nums: number[], t: number): number[] {
    // My thinking: same sliding window as countGe, but instead
    // of adding up the counts I keep, for each right end r, the
    // largest left end L with value >= t (or -1 when there is
    // none) — those are exactly the left ends whose subarrays
    // ending at r count towards the sum above the threshold.
    const n = nums.length;
    const maxd: number[] = [];
    const mind: number[] = [];
    let maxHead = 0;
    let minHead = 0;
    let left = 0;
    const out: number[] = [];
    for (let r = 0; r < n; r++) {
        while (maxd.length > maxHead && nums[maxd[maxd.length - 1]] <= nums[r]) maxd.pop();
        maxd.push(r);
        while (mind.length > minHead && nums[mind[mind.length - 1]] >= nums[r]) mind.pop();
        mind.push(r);
        while (left <= r && nums[maxd[maxHead]] - nums[mind[minHead]] >= t) {
            left++;
            while (maxd[maxHead] < left) maxHead++;
            while (mind[minHead] < left) minHead++;
        }
        out.push(left - 1);
    }
    return out;
}

class Extremes {
    isMax: boolean;
    nodes: number[][];

    // My thinking: for a fixed right end, the max (or min) over
    // [l..r] only changes at a few left ends, so I keep the
    // segments in a stack, each with its value, its rightmost
    // index, and the running sum up to that index. Appending a
    // new right end pops every segment the new value dominates
    // and merges them into one, so a prefix sum over [0..L] is
    // a binary search plus one multiplication.
    constructor(isMax: boolean) {
        this.isMax = isMax;
        this.nodes = [];
    }

    append(r: number, v: number): void {
        const nodes = this.nodes;
        let total = 1;
        while (nodes.length > 0) {
            const last = nodes[nodes.length - 1];
            const val = last[0];
            const right = last[1];
            if ((this.isMax && val <= v) || (!this.isMax && val >= v)) {
                const prevRight = nodes.length >= 2 ? nodes[nodes.length - 2][1] : -1;
                total += right - prevRight;
                nodes.pop();
            } else {
                break;
            }
        }
        const base = nodes.length > 0 ? nodes[nodes.length - 1][2] : 0;
        nodes.push([v, r, base + v * total]);
    }

    prefixSum(left: number): number {
        if (left < 0) return 0;
        const nodes = this.nodes;
        let lo = 0;
        let hi = nodes.length - 1;
        while (lo < hi) {
            const mid = Math.floor((lo + hi) / 2);
            if (nodes[mid][1] < left) lo = mid + 1;
            else hi = mid;
        }
        const val = nodes[lo][0];
        const prevRight = lo > 0 ? nodes[lo - 1][1] : -1;
        const prevPref = lo > 0 ? nodes[lo - 1][2] : 0;
        return prevPref + val * (left - prevRight);
    }
}

function maxTotalSubarrayValue(nums: number[], k: number): number {
    // My thinking: the k-th largest subarray value T* is
    // found by binary searching the threshold, since the
    // count of subarrays with value >= t falls as t rises.
    // Every subarray worth more than T* must be added in
    // full, and the rest of the k picks are all exactly T*.
    // The full sum comes from the segment stacks: for each
    // right end I add the sum of maxes minus the sum of
    // mins over exactly the left ends above the threshold.
    let hi = Math.max(...nums) - Math.min(...nums);
    let lo = 0;
    while (lo < hi) {
        const mid = Math.floor((lo + hi + 1) / 2);
        if (countGe(nums, mid) >= k) lo = mid;
        else hi = mid - 1;
    }
    const tStar = lo;
    const countGt = countGe(nums, tStar + 1);
    const limits = thresholds(nums, tStar + 1);
    const mx = new Extremes(true);
    const mn = new Extremes(false);
    let sumGt = 0;
    for (let r = 0; r < nums.length; r++) {
        mx.append(r, nums[r]);
        mn.append(r, nums[r]);
        if (limits[r] >= 0) sumGt += mx.prefixSum(limits[r]) - mn.prefixSum(limits[r]);
    }
    return sumGt + (k - countGt) * tStar;
}
