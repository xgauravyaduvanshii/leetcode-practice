/**
 * @param {number[]} locations
 * @param {number} start
 * @param {number} finish
 * @param {number} fuel
 * @return {number}
 */
var countRoutes = function(locations, start, finish, fuel) {
    // My thinking: from any city with fuel left you may
    // stop at the finish or drive on — so count the stop
    // plus every onward trip you can still afford.
    const MOD = 1000000007;
    const memo = new Map();
    function dp(pos, left) {
        const key = `${pos}|${left}`;
        const hit = memo.get(key);
        if (hit !== undefined) return hit;
        let total = pos === finish ? 1 : 0;
        for (let nxt = 0; nxt < locations.length; nxt++) {
            if (nxt === pos) continue;
            const cost = Math.abs(locations[pos] - locations[nxt]);
            if (cost <= left) total = (total + dp(nxt, left - cost)) % MOD;
        }
        memo.set(key, total);
        return total;
    }
    return dp(start, fuel);
};
