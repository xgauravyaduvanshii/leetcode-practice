// 2677. Chunk Array (Easy)
// https://leetcode.com/problems/chunk-array/
// Submission 2200144711 -- Accepted, JavaScript
// My thinking: step through the array in jumps of size and slice
// out each piece; the last slice is simply whatever is left.
var chunk = function(arr, size) {
    const chunks = [];
    for (let i = 0; i < arr.length; i += size) {
        chunks.push(arr.slice(i, i + size));
    }
    return chunks;
};
