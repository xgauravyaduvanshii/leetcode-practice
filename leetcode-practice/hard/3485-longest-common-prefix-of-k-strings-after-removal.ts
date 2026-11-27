// LeetCode 3485. Longest Common Prefix of K Strings After Removal — Hard
// https://leetcode.com/problems/longest-common-prefix-of-k-strings-after-removal/
// Submission 2202698911 — Accepted, TypeScript
function longestCommonPrefix(words: string[], k: number): number[] {
    // My thinking: the answer for the whole array is the deepest
    // trie node whose subtree holds at least k words, call that
    // depth D. Removing one word can only hurt a node on that
    // word's own path, and only if the node holds exactly k
    // words. So every answer is D unless the single deepest
    // k-node is unique and lies on the removed word's path.
    // For those words the answer is the best of two things: a
    // node holding at least k+1 words (it survives any single
    // removal), and the deepest k-node off the unique node's
    // root path (that path is shared by all such words, so one
    // value covers them all).
    const n = words.length;
    const children: Map<string, number>[] = [new Map()];
    const cnt: number[] = [0];
    const parent: number[] = [-1];
    const wordNodes: number[][] = [];
    for (const w of words) {
        let node = 0;
        const path = [0];
        for (const ch of w) {
            let nxt = children[node].get(ch);
            if (nxt === undefined) {
                nxt = children.length;
                children[node].set(ch, nxt);
                children.push(new Map());
                cnt.push(0);
                parent.push(node);
            }
            node = nxt;
            cnt[node] += 1;
            path.push(node);
        }
        wordNodes.push(path);
    }
    if (n < k) return new Array(n).fill(0);
    const depth: number[] = new Array(children.length).fill(0);
    const stack: number[] = [0];
    while (stack.length > 0) {
        const u = stack.pop()!;
        for (const v of children[u].values()) {
            depth[v] = depth[u] + 1;
            stack.push(v);
        }
    }
    let A = 0;
    let D = 0;
    for (let node = 1; node < children.length; node++) {
        if (cnt[node] >= k + 1) A = Math.max(A, depth[node]);
        if (cnt[node] >= k) D = Math.max(D, depth[node]);
    }
    const sD: number[] = [];
    for (let node = 1; node < children.length; node++) {
        if (depth[node] === D && cnt[node] >= k) sD.push(node);
    }
    if (sD.length >= 2) return new Array(n).fill(D);
    if (sD.length === 0) return new Array(n).fill(0);
    const uStar = sD[0];
    const anc = new Set<number>();
    let cur = uStar;
    while (cur !== -1) {
        anc.add(cur);
        cur = parent[cur];
    }
    let B = 0;
    for (let node = 1; node < children.length; node++) {
        if (depth[node] < D && cnt[node] >= k && !anc.has(node)) {
            B = Math.max(B, depth[node]);
        }
    }
    const ans: number[] = new Array(n).fill(0);
    for (let i = 0; i < n; i++) {
        ans[i] = wordNodes[i].includes(uStar) ? Math.max(A, B) : D;
    }
    return ans;
}
