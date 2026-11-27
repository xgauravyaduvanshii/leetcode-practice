// LeetCode 1776. Car Fleet II — Hard
// https://leetcode.com/problems/car-fleet-ii/
// Submission 2201158942 — Accepted, Go
//
// My thinking: I walk from the back, keeping the
// cars ahead that are still worth catching — a car
// I am slower than can never be caught, and a car
// that crashes into the fleet ahead of it before I
// would reach it is no longer the one I chase.

func getCollisionTimes(cars [][]int) []float64 {
    n := len(cars)
    ans := make([]float64, n)
    for i := range ans {
        ans[i] = -1
    }
    stack := []int{}
    for i := n - 1; i >= 0; i-- {
        pos, speed := cars[i][0], cars[i][1]
        for len(stack) > 0 {
            j := stack[len(stack)-1]
            posJ, speedJ := cars[j][0], cars[j][1]
            if speed <= speedJ {
                stack = stack[:len(stack)-1]
                continue
            }
            t := float64(posJ-pos) / float64(speed-speedJ)
            if ans[j] < 0 || t <= ans[j] {
                ans[i] = t
                break
            }
            stack = stack[:len(stack)-1]
        }
        stack = append(stack, i)
    }
    return ans
}
