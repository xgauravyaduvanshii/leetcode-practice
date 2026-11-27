// 2722. Join Two Arrays by ID (Medium)
// https://leetcode.com/problems/join-two-arrays-by-id/
// Submission 2201036975 -- Accepted, JavaScript
// My thinking: I merge both arrays by id, letting the
// second array's values win on shared keys, then sort
// the result by id.
var join = function(arr1, arr2) {
    const merged = {};
    for (const obj of arr1.concat(arr2)) {
        merged[obj.id] = { ...(merged[obj.id] || {}), ...obj };
    }
    return Object.values(merged).sort((a, b) => a.id - b.id);
};
