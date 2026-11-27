// 2631. Group By (Medium)
// https://leetcode.com/problems/group-by/
// Submission 2201036252 -- Accepted, JavaScript
// My thinking: I walk the array once and drop each item
// into a bucket named by its key — items with the same
// key end up together.
Array.prototype.groupBy = function(fn) {
    const groups = {};
    for (const item of this) {
        const key = fn(item);
        if (!(key in groups)) {
            groups[key] = [];
        }
        groups[key].push(item);
    }
    return groups;
};
