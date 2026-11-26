// LeetCode 3977. Minimum Time to Reach Target With Limited Power — Hard
// https://leetcode.com/problems/minimum-time-to-reach-target-with-limited-power/
// Submission 2203493761 — Accepted, Kotlin
class Solution {
    fun minTimeMaxPower(n: Int, edges: Array<IntArray>, power: Int, cost: IntArray, source: Int, target: Int): LongArray {
        // My thinking: a state is a node together with the
        // power left on arrival, and from it you may leave
        // only when the power covers the node's cost, paying
        // that cost and the edge time. Time strictly grows
        // along every edge, so Dijkstra over these states,
        // ordered by time and breaking ties by more
        // remaining power, settles each state once; the
        // first time the target is popped it has the
        // smallest time and, among those, the most power
        // left. A single label per node would be wrong: a
        // slower arrival with more power can still continue
        // where a faster, drained one cannot. PriorityQueue
        // needs no import here: it comes with the default
        // imports, and an explicit one would clash.
        val adj = Array(n) { mutableListOf<IntArray>() }
        for (e in edges) {
            adj[e[0]].add(intArrayOf(e[1], e[2]))
        }
        val INF = Long.MAX_VALUE / 4
        val dist = Array(n) { LongArray(power + 1) { INF } }
        dist[source][power] = 0L
        val pq = PriorityQueue<State>()
        pq.add(State(0L, power, source))
        while (pq.isNotEmpty()) {
            val cur = pq.poll()
            if (cur.time != dist[cur.node][cur.power]) continue
            if (cur.node == target) return longArrayOf(cur.time, cur.power.toLong())
            if (cur.power < cost[cur.node]) continue
            for ((v, t) in adj[cur.node]) {
                val np = cur.power - cost[cur.node]
                val nt = cur.time + t
                if (nt < dist[v][np]) {
                    dist[v][np] = nt
                    pq.add(State(nt, np, v))
                }
            }
        }
        return longArrayOf(-1L, -1L)
    }

    private data class State(val time: Long, val power: Int, val node: Int) : Comparable<State> {
        override fun compareTo(other: State): Int {
            if (time != other.time) return time.compareTo(other.time)
            return other.power.compareTo(power)
        }
    }
}
