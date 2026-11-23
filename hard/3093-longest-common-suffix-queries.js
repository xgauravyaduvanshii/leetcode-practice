// LeetCode 3093. Longest Common Suffix Queries — Hard
// https://leetcode.com/problems/longest-common-suffix-queries/
// Submission 2201987613 — Accepted, JavaScript
//
// My thinking: I build a trie of the
// container words spelled backwards, so
// walking it follows a common suffix.
// Each node remembers the shortest
// container word passing through it
// (earliest on a tie). A query walks
// the reversed trie as far as it
// matches and takes the word stored
// at the deepest node reached.

/**
 * @param {string[]} wordsContainer
 * @param {string[]} wordsQuery
 * @return {number[]}
 */
var stringIndices = function(wordsContainer, wordsQuery) {
    const lengths = wordsContainer.map(w => w.length);
    const children = [new Map()];
    const best = [-1];
    function update(node, i) {
        const b = best[node];
        if (b === -1 || lengths[i] < lengths[b]) best[node] = i;
    }
    wordsContainer.forEach((w, i) => {
        let node = 0;
        update(node, i);
        for (let j = w.length - 1; j >= 0; --j) {
            const ch = w[j];
            let nxt = children[node].get(ch);
            if (nxt === undefined) {
                nxt = children.length;
                children[node].set(ch, nxt);
                children.push(new Map());
                best.push(-1);
            }
            node = nxt;
            update(node, i);
        }
    });
    const ans = [];
    for (const q of wordsQuery) {
        let node = 0;
        for (let j = q.length - 1; j >= 0; --j) {
            const nxt = children[node].get(q[j]);
            if (nxt === undefined) break;
            node = nxt;
        }
        ans.push(best[node]);
    }
    return ans;
};
