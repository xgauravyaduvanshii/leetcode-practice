# LeetCode 2284. Sender With Largest Word Count — Medium
# https://leetcode.com/problems/sender-with-largest-word-count/
# Submission 2204636626 — Accepted, Python3
#
# My thinking: count each sender's words by splitting their messages on
# whitespace and adding the word counts. The winner is the sender with
# the highest total; on a tie the lexicographically largest sender name
# wins, which is exactly what max() over (count, name) pairs gives.
class Solution:
    def largestWordCount(self, messages: list[str], senders: list[str]) -> str:
        counts = {}
        for msg, sender in zip(messages, senders):
            counts[sender] = counts.get(sender, 0) + len(msg.split())
        return max(counts.items(), key=lambda kv: (kv[1], kv[0]))[0]
