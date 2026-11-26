// LeetCode 12. Integer to Roman — Medium
// https://leetcode.com/problems/integer-to-roman/
// Submission 2203804616 — Accepted, TypeScript

// My thinking: I walk the Roman symbols from largest to smallest and
// take as many of each as fit, which works because the symbols are
// listed in decreasing value and the subtractive pairs (IV, IX, XL,
// XC, CD, CM) are included as symbols of their own. Whatever is left
// after one symbol is handled by the smaller ones.
function intToRoman(num: number): string {
    const symbols: [number, string][] = [
        [1000, 'M'], [900, 'CM'], [500, 'D'], [400, 'CD'],
        [100, 'C'], [90, 'XC'], [50, 'L'], [40, 'XL'],
        [10, 'X'], [9, 'IX'], [5, 'V'], [4, 'IV'], [1, 'I'],
    ];
    let out = '';
    for (const [value, symbol] of symbols) {
        const count = Math.floor(num / value);
        out += symbol.repeat(count);
        num -= value * count;
    }
    return out;
}
