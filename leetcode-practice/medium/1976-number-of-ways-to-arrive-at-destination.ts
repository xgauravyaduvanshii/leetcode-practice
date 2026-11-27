// LeetCode 1976. Number of Ways to Arrive at Destination — Medium
// https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/
// Submission 2204089227 — Accepted, TypeScript

// My thinking: This is a shortest-path counting problem, so Dijkstra's
// algorithm finds the shortest travel time from intersection 0 to every
// other intersection. Along the way I also keep, for each intersection,
// how many different shortest routes reach it.
// When I relax an edge and find a strictly shorter time to a neighbour,
// that neighbour's shortest time becomes the new time and its count
// resets to the count of the node I came from — every shortest route to
// the neighbour must now go through that node.
// When I relax an edge and find a time exactly equal to the neighbour's
// current shortest time, I have found more shortest routes, so I add
// the count of the node I came from to the neighbour's count.
// A longer time is ignored, since it can never be part of a shortest
// route. All counts are taken modulo 1_000_000_007, and the answer is
// the count stored for intersection n - 1.
function countPaths(n: number, roads: number[][]): number {
    const MOD = 1_000_000_007;

    const graph: [number, number][][] = Array.from({ length: n }, () => []);
    for (const [u, v, time] of roads) {
        graph[u].push([v, time]);
        graph[v].push([u, time]);
    }

    const dist: number[] = new Array(n).fill(Infinity);
    const ways: number[] = new Array(n).fill(0);
    dist[0] = 0;
    ways[0] = 1;

    // A small priority queue of [travel time so far, intersection],
    // kept sorted by time so the closest unvisited node comes out first.
    const heap: [number, number][] = [[0, 0]];
    const popMin = (): [number, number] => {
        let best = 0;
        for (let i = 1; i < heap.length; i++) {
            if (heap[i][0] < heap[best][0]) best = i;
        }
        return heap.splice(best, 1)[0];
    };

    while (heap.length > 0) {
        const [time, node] = popMin();
        if (time > dist[node]) continue;
        for (const [neighbour, travel] of graph[node]) {
            const newTime = time + travel;
            if (newTime < dist[neighbour]) {
                dist[neighbour] = newTime;
                ways[neighbour] = ways[node];
                heap.push([newTime, neighbour]);
            } else if (newTime === dist[neighbour]) {
                ways[neighbour] = (ways[neighbour] + ways[node]) % MOD;
            }
        }
    }

    return ways[n - 1] % MOD;
}
