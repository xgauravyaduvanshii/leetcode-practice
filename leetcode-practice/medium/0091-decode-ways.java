// LeetCode 91. Decode Ways — Medium
// https://leetcode.com/problems/decode-ways/
// Submission 2203969559 — Accepted, Java

// My thinking: I walk the string left to right, keeping one number —
// how many ways the prefix so far can be decoded. At each position I
// look at the current digit alone and at the last two digits together.
// A single digit decodes on its own only when it is not '0', because
// '0' has no letter of its own. A pair decodes as one letter only when
// it is between 10 and 26, so '06' is never a pair and '27' is not
// either. I add the single-digit ways when the digit is valid and the
// pair ways when the pair is valid, carrying just the last two counts
// forward instead of a whole table. One pass, constant space.
class Solution {
    public int numDecodings(String s) {
        // ways for the empty prefix, and for the first character
        int prev2 = 1;
        int prev1 = s.charAt(0) == '0' ? 0 : 1;
        for (int i = 1; i < s.length(); i++) {
            int current = 0;
            // decode s.charAt(i) on its own, only if it is not '0'
            if (s.charAt(i) != '0') {
                current += prev1;
            }
            // decode the last two digits as one letter, only for 10..26
            int twoDigit = (s.charAt(i - 1) - '0') * 10 + (s.charAt(i) - '0');
            if (twoDigit >= 10 && twoDigit <= 26) {
                current += prev2;
            }
            prev2 = prev1;
            prev1 = current;
        }
        return prev1;
    }
}
