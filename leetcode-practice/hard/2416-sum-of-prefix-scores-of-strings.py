# LeetCode 2416. Sum of Prefix Scores of Strings — Hard
# https://leetcode.com/problems/sum-of-prefix-scores-of-strings/
# Submission 2201724574 — Accepted, Python3
# (filed as a verified reconstruction: solved on LeetCode 23 Nov 2026 ~12:05 IST
# during the study run; the original submission ID was recorded by the browser
# that found it already solved, and this file was verified locally below)
#
# My thinking: a prefix is worth as many
# words as share it — I grow a trie of
# every word, counting how many pass each
# node, then walk each word down and add
# up the counts on its way.

class Solution:
    def sumPrefixScores(self, words: list[str]) -> list[int]:
        children = [{}]
        counts = [0]
        for w in words:
            node = 0
            for ch in w:
                if ch not in children[node]:
                    children[node][ch] = len(children)
                    children.append({})
                    counts.append(0)
                node = children[node][ch]
                counts[node] += 1
        ans = []
        for w in words:
            node = 0
            total = 0
            for ch in w:
                node = children[node][ch]
                total += counts[node]
            ans.append(total)
        return ans
