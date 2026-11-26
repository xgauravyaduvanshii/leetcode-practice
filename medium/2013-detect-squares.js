// LeetCode 2013. Detect Squares — Medium
// https://leetcode.com/problems/detect-squares/
// Submission 2204139326 — Accepted, JavaScript

// My thinking:
// I keep a count of every point added so far, keyed by its "x,y" coordinates,
// because the same point can be added more than once and each copy counts.
// To count squares with a query point as one corner, I look for a second point
// straight above or below it on the same x — that gives me the side length of
// a possible square. For a vertical side of length d, the other two corners
// must sit d units to the left or to the right, at the same two y-values.
// So for each point (x, y2) sharing the query point's x, I check both the
// left and right columns: the number of squares through that pair is the
// product of the three point counts — the vertical partner and the two
// corners in the other column. Adding those products up over all vertical
// partners gives the answer. There are at most a few hundred distinct points
// on one column, so this is fast enough.

/**
 * DetectSquares
 */
var DetectSquares = function() {
    this.counts = new Map();
};

DetectSquares.prototype.add = function(point) {
    const key = point[0] + ',' + point[1];
    this.counts.set(key, (this.counts.get(key) || 0) + 1);
};

DetectSquares.prototype.count = function(point) {
    const [x, y] = point;
    const get = (px, py) => this.counts.get(px + ',' + py) || 0;
    let total = 0;
    for (const [key, c] of this.counts) {
        const [px, py] = key.split(',').map(Number);
        if (px !== x || py === y) continue;
        const d = Math.abs(py - y);
        // Squares to the right of the vertical side.
        total += c * get(x + d, y) * get(x + d, py);
        // Squares to the left of the vertical side.
        total += c * get(x - d, y) * get(x - d, py);
    }
    return total;
};

/**
 * Your DetectSquares object will be instantiated and called as such:
 * var obj = new DetectSquares()
 * obj.add(point)
 * var param_2 = obj.count(point)
 */
