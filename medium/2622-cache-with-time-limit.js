// 2622. Cache With Time Limit (Medium)
// https://leetcode.com/problems/cache-with-time-limit/
// Submission 2201030331 -- Accepted, JavaScript
// My thinking: I store each value with its expiry time —
// a key only counts if its expiry is still in the future.
var TimeLimitedCache = function() {
    this.cache = new Map();
};

TimeLimitedCache.prototype.set = function(key, value, duration) {
    const existing = this.cache.get(key);
    const existed = existing !== undefined && existing.expiry > Date.now();
    const expiry = Date.now() + duration;
    this.cache.set(key, { value, expiry });
    return existed;
};

TimeLimitedCache.prototype.get = function(key) {
    const entry = this.cache.get(key);
    if (entry !== undefined && entry.expiry > Date.now()) {
        return entry.value;
    }
    return -1;
};

TimeLimitedCache.prototype.count = function() {
    const now = Date.now();
    let count = 0;
    for (const entry of this.cache.values()) {
        if (entry.expiry > now) {
            count++;
        }
    }
    return count;
};
