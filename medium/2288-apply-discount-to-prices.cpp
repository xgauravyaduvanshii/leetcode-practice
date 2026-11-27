// LeetCode 2288. Apply Discount to Prices — Medium
// https://leetcode.com/problems/apply-discount-to-prices/
// Submission 2204644864 — Accepted, C++
//
// My thinking: same idea as the Python version — split on spaces, treat
// a word as a price only when it is '$' followed by digits only, and do
// the discount in integer cents (price * (100 - discount)) so no
// floating-point rounding creeps in. Cents below 10 get a leading zero.
class Solution {
public:
    string discountPrices(string sentence, int discount) {
        vector<string> words;
        string cur;
        for (char c : sentence) {
            if (c == ' ') {
                words.push_back(cur);
                cur.clear();
            } else {
                cur += c;
            }
        }
        words.push_back(cur);
        string ans;
        for (int i = 0; i < (int)words.size(); i++) {
            string w = words[i];
            bool isPrice = w.size() > 1 && w[0] == '$';
            for (int j = 1; j < (int)w.size() && isPrice; j++) {
                if (!isdigit((unsigned char)w[j])) isPrice = false;
            }
            if (isPrice) {
                long long cents = stoll(w.substr(1)) * (100 - discount);
                string s = "$" + to_string(cents / 100) + ".";
                long long rem = cents % 100;
                if (rem < 10) s += "0";
                s += to_string(rem);
                ans += s;
            } else {
                ans += w;
            }
            if (i + 1 < (int)words.size()) ans += " ";
        }
        return ans;
    }
};
