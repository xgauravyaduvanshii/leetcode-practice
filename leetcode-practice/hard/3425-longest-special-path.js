// LeetCode 3425. Longest Special Path — Hard
// https://leetcode.com/problems/longest-special-path/
// Submission 2202523842 — Accepted 675/675, JavaScript
/**
 * @param {number[][]} edges
 * @param {number[]} nums
 * @return {number[]}
 */
var longestSpecialPath = function(edges, nums) {
    // My thinking: on a root-to-leaf walk I keep the depth of
    // the last sighting of every value, so the earliest start
    // of a special path ending at the current node is just
    // past the deepest repeated value on that walk. The length
    // is the prefix-distance difference to that start, and the
    // node count is the depth difference — I keep the longest
    // length, breaking ties by the fewest nodes. An iterative
    // walk avoids recursion limits on deep trees.
    const n = nums.length;
    const graph = Array.from({length: n}, () => []);
    for (const [u, v, w] of edges) {
        graph[u].push([v, w]);
        graph[v].push([u, w]);
    }
    let bestLen = 0;
    let bestNodes = 1;
    const last = new Map();
    const distAtDepth = [];

    const enter = (u, depth, dist, limit) => {
        distAtDepth.push(dist);
        const old = last.has(nums[u]) ? last.get(nums[u]) : undefined;
        last.set(nums[u], depth);
        const length = dist - distAtDepth[limit + 1];
        const nodes = depth - limit;
        if (length > bestLen || (length === bestLen && nodes < bestNodes)) {
            bestLen = length;
            bestNodes = nodes;
        }
        return old;
    };

    // frame: [node, parent, depth, dist, limit, nextChildIdx, oldLast]
    const stack = [[0, -1, 0, 0, -1, 0, enter(0, 0, 0, -1)]];
    while (stack.length > 0) {
        const frame = stack[stack.length - 1];
        const [u, parent, depth, dist, limit, ci, old] = frame;
        if (ci < graph[u].length) {
            const [v, w] = graph[u][ci];
            frame[5] += 1;
            if (v === parent) continue;
            const nlimit = Math.max(limit, last.has(nums[v]) ? last.get(nums[v]) : -1);
            stack.push([v, u, depth + 1, dist + w, nlimit, 0,
                        enter(v, depth + 1, dist + w, nlimit)]);
        } else {
            stack.pop();
            distAtDepth.pop();
            if (old === undefined) last.delete(nums[u]);
            else last.set(nums[u], old);
        }
    }
    return [bestLen, bestNodes];
};
