// LeetCode 3873. Maximum Points Activated with One Addition — Hard
// https://leetcode.com/problems/maximum-points-activated-with-one-addition/
// Submission 2203332805 — Accepted, Kotlin
class Solution {
    fun maxActivated(points: Array<IntArray>): Int {
        // My thinking: activation spreads along shared x or y
        // coordinates, so the points split into connected
        // components where two points are linked when they
        // share an x or a y — a union-find over the points,
        // joining each point to the first point seen with its
        // x and with its y, finds them. Adding one point at
        // (X, Y) activates every point with x = X and every
        // point with y = Y, and then the whole components
        // those points belong to. All points sharing an x
        // (or a y) already sit in one component, so the new
        // point touches at most two components, and any two
        // components can be bridged this way: pick X from
        // one component's x-coordinates and Y from the
        // other's y-coordinates, and (X, Y) cannot already
        // be a point or the two components would be one.
        // The best play is therefore 1 (the new point) plus
        // the sizes of the two largest components.
        val n = points.size
        val parent = IntArray(n) { it }
        val size = IntArray(n) { 1 }

        fun find(x: Int): Int {
            var v = x
            while (parent[v] != v) {
                parent[v] = parent[parent[v]]
                v = parent[v]
            }
            return v
        }

        fun union(a: Int, b: Int) {
            var ra = find(a)
            var rb = find(b)
            if (ra == rb) return
            if (size[ra] < size[rb]) {
                val tmp = ra
                ra = rb
                rb = tmp
            }
            parent[rb] = ra
            size[ra] += size[rb]
        }

        val byX = HashMap<Int, Int>()
        val byY = HashMap<Int, Int>()
        for (i in 0 until n) {
            val x = points[i][0]
            val y = points[i][1]
            val px = byX[x]
            if (px != null) union(i, px) else byX[x] = i
            val py = byY[y]
            if (py != null) union(i, py) else byY[y] = i
        }

        val compSize = HashMap<Int, Int>()
        for (i in 0 until n) {
            val root = find(i)
            compSize[root] = (compSize[root] ?: 0) + 1
        }
        var best1 = 0
        var best2 = 0
        for (s in compSize.values) {
            if (s > best1) {
                best2 = best1
                best1 = s
            } else if (s > best2) {
                best2 = s
            }
        }
        return 1 + best1 + best2
    }
}
