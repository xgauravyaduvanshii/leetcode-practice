// LeetCode 3273. Minimum Amount of Damage Dealt to Bob — Hard
// https://leetcode.com/problems/minimum-amount-of-damage-dealt-to-bob/
// Submission 2202172754 — Accepted, Go
//
// My thinking: an enemy with health h takes
// ceil(h / power) seconds to kill, dealing its
// damage every second until it dies. Killing
// the enemy with the smaller time-per-damage
// first is always better, so I sort by t / d
// (compared cross-multiplied, no floats) and
// accumulate: each enemy adds its damage times
// the total time elapsed so far.

import "sort"

func minDamage(power int, damage []int, health []int) int64 {
    type enemy struct {
        t, d int64
    }
    enemies := make([]enemy, len(damage))
    for i := range damage {
        t := int64((health[i] + power - 1) / power)
        enemies[i] = enemy{t, int64(damage[i])}
    }
    sort.Slice(enemies, func(i, j int) bool {
        return enemies[i].t*enemies[j].d < enemies[j].t*enemies[i].d
    })
    var cur, ans int64
    for _, e := range enemies {
        cur += e.t
        ans += e.d * cur
    }
    return ans
}
