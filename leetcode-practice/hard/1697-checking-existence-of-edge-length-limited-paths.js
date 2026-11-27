// LeetCode 1697. Checking Existence of Edge Length Limited Paths — Hard
// https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/
// Submission 2201098386 — Accepted, JavaScript
//
// My thinking: I sort the edges and the queries by
// their limits, then sweep through adding edges to a
// union-find as their weight becomes allowed — a query
// is answered by whether its two ends are already
// connected when its limit is reached.

var distanceLimitedPathsExist = function(n, edgeList, queries) {
    const parent = Array.from({length: n}, (_, i) => i);
    const find = (x) => {
        while (parent[x] !== x) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    };
    edgeList.sort((a, b) => a[2] - b[2]);
    const order = queries.map((_, i) => i).sort((a, b) => queries[a][2] - queries[b][2]);
    const answer = new Array(queries.length).fill(false);
    let e = 0;
    for (const i of order) {
        const [p, q, limit] = queries[i];
        while (e < edgeList.length && edgeList[e][2] < limit) {
            const ra = find(edgeList[e][0]);
            const rb = find(edgeList[e][1]);
            if (ra !== rb) parent[ra] = rb;
            e++;
        }
        answer[i] = find(p) === find(q);
    }
    return answer;
};
