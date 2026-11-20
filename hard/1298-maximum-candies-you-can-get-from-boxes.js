/**
 * @param {number[]} status
 * @param {number[]} candies
 * @param {number[][]} keys
 * @param {number[][]} containedBoxes
 * @param {number[]} initialBoxes
 * @return {number}
 */
var maxCandies = function(status, candies, keys, containedBoxes, initialBoxes) {
    // My thinking: keep every box we hold; open the ones we
    // have keys for, and whenever a new key or a new box
    // arrives, retry the boxes still waiting.
    const n = status.length;
    const have = new Array(n).fill(false);
    const opened = new Array(n).fill(false);
    const hasKey = status.map(s => s === 1);
    const queue = [...initialBoxes];
    for (const box of initialBoxes) have[box] = true;
    let total = 0;
    while (queue.length > 0) {
        const box = queue.shift();
        if (opened[box] || !hasKey[box]) continue;
        opened[box] = true;
        total += candies[box];
        for (const key of keys[box]) {
            if (!hasKey[key]) {
                hasKey[key] = true;
                if (have[key] && !opened[key]) queue.push(key);
            }
        }
        for (const inner of containedBoxes[box]) {
            if (!have[inner]) {
                have[inner] = true;
                if (hasKey[inner]) queue.push(inner);
            }
        }
    }
    return total;
};
