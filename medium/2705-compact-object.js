// 2705. Compact Object (Medium)
// https://leetcode.com/problems/compact-object/
// Submission 2201039265 -- Accepted, JavaScript
// My thinking: I rebuild the value from scratch, keeping
// only the entries that are truthy and compacting the
// nested ones the same way.
var compactObject = function(obj) {
    if (Array.isArray(obj)) {
        return obj.filter(Boolean).map(compactObject);
    }
    if (obj !== null && typeof obj === "object") {
        const result = {};
        for (const key of Object.keys(obj)) {
            const value = compactObject(obj[key]);
            if (value) {
                result[key] = value;
            }
        }
        return result;
    }
    return obj;
};
