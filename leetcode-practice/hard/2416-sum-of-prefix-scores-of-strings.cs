// LeetCode 2416. Sum of Prefix Scores of Strings — Hard
// https://leetcode.com/problems/sum-of-prefix-scores-of-strings/
// Submission 2201730651 — Accepted, C#
//
// My thinking: a prefix is worth as many
// words as share it — I grow a trie of
// every word, counting how many pass each
// node, then walk each word down and add
// up the counts on its way.

using System;
using System.Collections.Generic;

public class Solution {
    private class TrieNode {
        public Dictionary<char, TrieNode> Children = new Dictionary<char, TrieNode>();
        public int Count = 0;
    }

    public int[] SumPrefixScores(string[] words) {
        var root = new TrieNode();
        foreach (var w in words) {
            var node = root;
            foreach (var ch in w) {
                if (!node.Children.TryGetValue(ch, out var next)) {
                    next = new TrieNode();
                    node.Children[ch] = next;
                }
                node = next;
                node.Count++;
            }
        }
        var ans = new int[words.Length];
        for (int i = 0; i < words.Length; i++) {
            var node = root;
            int total = 0;
            foreach (var ch in words[i]) {
                node = node.Children[ch];
                total += node.Count;
            }
            ans[i] = total;
        }
        return ans;
    }
}
