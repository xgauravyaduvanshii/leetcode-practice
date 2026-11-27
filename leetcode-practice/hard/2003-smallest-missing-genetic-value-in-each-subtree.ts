// LeetCode 2003. Smallest Missing Genetic Value in Each Subtree — Hard
// https://leetcode.com/problems/smallest-missing-genetic-value-in-each-subtree/
// Submission 2201308834 — Accepted, TypeScript
//
// My thinking: only the nodes above the 1 can
// miss anything but 1, so I walk up from the 1
// gathering each new branch once — the missing
// value only ever climbs.

function smallestMissingValueSubtree(parents: number[], nums: number[]): number[] {
    const n = parents.length;
    const children: number[][] = Array.from({ length: n }, () => []);
    let node1 = -1;
    for (let i = 0; i < n; i++) {
        if (parents[i] !== -1) children[parents[i]].push(i);
        if (nums[i] === 1) node1 = i;
    }
    const ans = new Array(n).fill(1);
    if (node1 === -1) return ans;
    const seen = new Set<number>();
    let mex = 1;
    const addSubtree = (u: number) => {
        const stack = [u];
        while (stack.length) {
            const x = stack.pop()!;
            seen.add(nums[x]);
            for (const c of children[x]) stack.push(c);
        }
    };
    addSubtree(node1);
    let node = node1;
    while (true) {
        while (seen.has(mex)) mex++;
        ans[node] = mex;
        const p = parents[node];
        if (p === -1) break;
        seen.add(nums[p]);
        for (const c of children[p]) {
            if (c !== node) addSubtree(c);
        }
        node = p;
    }
    return ans;
}
