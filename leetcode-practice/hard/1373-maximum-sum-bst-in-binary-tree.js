/**
 * @param {TreeNode} root
 * @return {number}
 */
var maxSumBST = function(root) {
    // My thinking: a subtree is a search tree when its left
    // side stays below and its right side above — so each
    // subtree reports whether it qualifies, its range and
    // its sum, and the best sum seen anywhere wins.
    let best = 0;
    function dfs(node) {
        if (node === null) return [true, Infinity, -Infinity, 0];
        const [leftBst, leftMin, leftMax, leftSum] = dfs(node.left);
        const [rightBst, rightMin, rightMax, rightSum] = dfs(node.right);
        if (leftBst && rightBst && leftMax < node.val && node.val < rightMin) {
            const total = leftSum + rightSum + node.val;
            best = Math.max(best, total);
            return [true, Math.min(leftMin, node.val), Math.max(rightMax, node.val), total];
        }
        return [false, 0, 0, 0];
    }
    dfs(root);
    return best;
};
