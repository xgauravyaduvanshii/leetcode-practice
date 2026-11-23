// LeetCode 2458. Height of Binary Tree After Subtree Removal Queries — Hard
// https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries/
// Submission 2201755253 — Accepted, TypeScript
//
// My thinking: removing a subtree leaves
// the rest of the tree standing, and its
// height is either what survives above
// the cut or the tallest sibling branch
// left behind — I walk down once, carrying
// that best surviving height to each child.

function treeQueries(root: TreeNode | null, queries: number[]): number[] {
    const depth = new Map<number, number>();
    const height = new Map<number, number>();
    const ans = new Map<number, number>();
    function dfs(u: TreeNode | null, d: number): number {
        if (!u) return -1;
        depth.set(u.val, d);
        let h = 0;
        for (const child of [u.left, u.right]) {
            if (child) h = Math.max(h, 1 + dfs(child, d + 1));
        }
        height.set(u.val, h);
        return h;
    }
    dfs(root, 0);
    function solve(u: TreeNode | null, up: number): void {
        if (!u) return;
        ans.set(u.val, up);
        const kids = [u.left, u.right].filter((c): c is TreeNode => c !== null);
        for (const child of kids) {
            let bestSib = -1;
            for (const sib of kids) {
                if (sib !== child) bestSib = Math.max(bestSib, height.get(sib.val)!);
            }
            solve(child, Math.max(up, depth.get(u.val)! + 1 + bestSib));
        }
    }
    solve(root, -1);
    return queries.map(q => ans.get(q)!);
}
