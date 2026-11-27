// LeetCode 2157. Groups of Strings — Hard
// https://leetcode.com/problems/groups-of-strings/
// Submission 2201594409 — Accepted, JavaScript
//
// My thinking: a word is just the set of its
// letters, so two words belong together when
// their sets are the same, differ by one
// letter, or swap one letter for another — I
// flip each letter in turn, and swap each
// letter for every letter it lacks, join
// whatever I find, and count the groups.

/**
 * @param {string[]} words
 * @return {number[]}
 */
var groupStrings = function(words) {
    const masks = words.map(w => {
        let m = 0;
        for (const ch of w) m |= 1 << (ch.charCodeAt(0) - 97);
        return m;
    });
    const index = new Map();
    const parent = words.map((_, i) => i);
    function find(x) {
        while (parent[x] !== x) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    }
    function union(a, b) {
        const ra = find(a), rb = find(b);
        if (ra !== rb) parent[ra] = rb;
    }
    for (let i = 0; i < masks.length; i++) {
        const m = masks[i];
        // Same set of letters: the words are identical.
        if (index.has(m)) union(i, index.get(m));
        else index.set(m, i);
        for (let b = 0; b < 26; b++) {
            // Add or delete one letter.
            const other = m ^ (1 << b);
            if (index.has(other)) union(i, index.get(other));
            // Replace one letter with a letter it lacks.
            if ((m >> b) & 1) {
                for (let c = 0; c < 26; c++) {
                    if (!((m >> c) & 1)) {
                        const rep = m ^ (1 << b) ^ (1 << c);
                        if (index.has(rep)) union(i, index.get(rep));
                    }
                }
            }
        }
    }
    const groups = new Map();
    for (let i = 0; i < words.length; i++) {
        const r = find(i);
        groups.set(r, (groups.get(r) ?? 0) + 1);
    }
    return [groups.size, Math.max(...groups.values())];
};
