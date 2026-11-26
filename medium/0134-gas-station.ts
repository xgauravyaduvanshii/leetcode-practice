// LeetCode 134. Gas Station — Medium
// https://leetcode.com/problems/gas-station/
// Submission 2204038538 — Accepted, TypeScript

// My thinking: if the total gas is less than the total cost, no
// starting station can work, so I return -1 straight away. Otherwise
// a solution is guaranteed, and I walk the stations once, keeping a
// running tank. Whenever the tank goes negative, every station from
// the current start up to here is a dead end — the tank only got
// worse along the way — so I move the start to the next station and
// reset the tank. The start left standing at the end is the answer.
function canCompleteCircuit(gas: number[], cost: number[]): number {
    const totalGas = gas.reduce((sum, g) => sum + g, 0);
    const totalCost = cost.reduce((sum, c) => sum + c, 0);
    if (totalGas < totalCost) {
        return -1;
    }
    let start = 0;
    let tank = 0;
    for (let i = 0; i < gas.length; i++) {
        tank += gas[i] - cost[i];
        if (tank < 0) {
            start = i + 1;
            tank = 0;
        }
    }
    return start;
}
