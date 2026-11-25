// LeetCode 3762. Minimum Operations to Equalize Subarrays — Hard
// https://leetcode.com/problems/minimum-operations-to-equalize-subarrays/
// Submission 2203163661 — Accepted, TypeScript
function minOperations(nums: number[], k: number, queries: number[][]): number[] {
    // My thinking: changing an element by steps of k can
    // only reach values in its own residue class mod k, so
    // a query is impossible when its range mixes residues
    // — a prefix count of residue changes spots that in
    // O(1). Otherwise every value in the range shares one
    // residue, and the cheapest target is a median of the
    // range: the cost is the sum of absolute deviations
    // from the median, divided by k. A persistent segment
    // tree over the compressed values gives, for any range,
    // its median by rank and the count and sum of values
    // below it, so each query costs O(log n) after one
    // O(n log n) build.
    const n = nums.length;
    const vals = [...new Set(nums)].sort((a, b) => a - b);
    const comp = new Map<number, number>();
    vals.forEach((v, i) => comp.set(v, i));
    const m = vals.length;
    const left: number[] = [0];
    const right: number[] = [0];
    const cnt: number[] = [0];
    const ssum: number[] = [0];
    function update(prev: number, l: number, r: number, pos: number, val: number): number {
        const idx = cnt.length;
        cnt.push(cnt[prev] + 1);
        ssum.push(ssum[prev] + val);
        left.push(0);
        right.push(0);
        if (l !== r) {
            const mid = Math.floor((l + r) / 2);
            if (pos <= mid) {
                left[idx] = update(left[prev], l, mid, pos, val);
                right[idx] = right[prev];
            } else {
                left[idx] = left[prev];
                right[idx] = update(right[prev], mid + 1, r, pos, val);
            }
        }
        return idx;
    }
    const roots: number[] = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) {
        roots[i + 1] = update(roots[i], 0, m - 1, comp.get(nums[i])!, nums[i]);
    }
    function kth(nodeR: number, nodeL: number, l: number, r: number, rank: number): number {
        while (l !== r) {
            const mid = Math.floor((l + r) / 2);
            const c = cnt[left[nodeR]] - cnt[left[nodeL]];
            if (rank <= c) {
                nodeR = left[nodeR];
                nodeL = left[nodeL];
                r = mid;
            } else {
                rank -= c;
                nodeR = right[nodeR];
                nodeL = right[nodeL];
                l = mid + 1;
            }
        }
        return l;
    }
    function prefix(nodeR: number, nodeL: number, l: number, r: number, qr: number): [number, number] {
        if (qr < l) return [0, 0];
        if (r <= qr) return [cnt[nodeR] - cnt[nodeL], ssum[nodeR] - ssum[nodeL]];
        const mid = Math.floor((l + r) / 2);
        const [c1, s1] = prefix(left[nodeR], left[nodeL], l, mid, qr);
        const [c2, s2] = prefix(right[nodeR], right[nodeL], mid + 1, r, qr);
        return [c1 + c2, s1 + s2];
    }
    const prefSum: number[] = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) prefSum[i + 1] = prefSum[i] + nums[i];
    const bad: number[] = new Array(n + 1).fill(0);
    for (let i = 1; i < n; i++) {
        bad[i + 1] = bad[i] + (nums[i] % k !== nums[i - 1] % k ? 1 : 0);
    }
    // bad[i] counts residue changes among indices < i, so
    // the changes inside [l, r] are bad[r + 1] - bad[l + 1].
    const ans: number[] = [];
    for (const [l, r] of queries) {
        if (bad[r + 1] - bad[l + 1] > 0) {
            ans.push(-1);
            continue;
        }
        const length = r - l + 1;
        const mi = kth(roots[r + 1], roots[l], 0, m - 1, Math.floor((length + 1) / 2));
        const med = vals[mi];
        const [cntLe, sumLe] = prefix(roots[r + 1], roots[l], 0, m - 1, mi);
        const cntGt = length - cntLe;
        const sumGt = (prefSum[r + 1] - prefSum[l]) - sumLe;
        const cost = med * cntLe - sumLe + sumGt - med * cntGt;
        ans.push(Math.floor(cost / k));
    }
    return ans;
}
