// LeetCode 4100. Minimum Cost Path With Even XOR Parity — Hard
// https://leetcode.com/problems/minimum-cost-path-with-even-xor-parity/
// Submission 2203732676 — Accepted, Go
import "math/bits"

func minActivationCost(edges [][]int, values []int) int {
    // My thinking: the XOR of a path has an even
    // number of set bits exactly when the number of
    // nodes on the path whose value has odd parity
    // (odd number of set bits) is even. So a path
    // is Balanced-XOR when it contains an even
    // count of parity-1 nodes. Any single edge
    // joining two nodes of equal parity has zero
    // parity-1 nodes on its two endpoints, so it
    // is already balanced — the cheapest such edge
    // is a candidate answer. Otherwise a balanced
    // path needs at least two parity-1 nodes, and
    // the cheapest such path has exactly two edges:
    // 1 - 0 - 1, going through a parity-0 middle
    // node. For each parity-0 node, keep its two
    // cheapest edges to parity-1 neighbors; their
    // sum is the cheapest 1-0-1 path through it.
    // The answer is the smaller of the cheapest
    // balanced edge and the cheapest 1-0-1 path,
    // or -1 when neither exists.
    n := len(values)
    parity := make([]int, n)
    for i, v := range values {
        parity[i] = bits.OnesCount(uint(v)) & 1
    }
    const INF int64 = 1 << 60
    ans := INF
    best1 := make([]int64, n)
    best2 := make([]int64, n)
    for i := range best1 {
        best1[i] = INF
        best2[i] = INF
    }
    for _, e := range edges {
        u, v := e[0], e[1]
        c := int64(e[2])
        if parity[u] == parity[v] && c < ans {
            ans = c
        }
        if parity[u] == 0 && parity[v] == 1 {
            if c < best1[u] {
                best2[u] = best1[u]
                best1[u] = c
            } else if c < best2[u] {
                best2[u] = c
            }
        }
        if parity[v] == 0 && parity[u] == 1 {
            if c < best1[v] {
                best2[v] = best1[v]
                best1[v] = c
            } else if c < best2[v] {
                best2[v] = c
            }
        }
    }
    for i := 0; i < n; i++ {
        if parity[i] == 0 && best2[i] < INF {
            if s := best1[i] + best2[i]; s < ans {
                ans = s
            }
        }
    }
    if ans == INF {
        return -1
    }
    return int(ans)
}
