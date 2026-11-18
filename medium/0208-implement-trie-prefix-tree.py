# LeetCode 208. Implement Trie - Prefix Tree — Medium
# https://leetcode.com/problems/implement-trie-prefix-tree/
# Submission 2198449320 — Accepted, Python3
#
# My thinking: each node of the trie holds the next
# letters that can follow it, and a flag for
# whether a word ends there. Inserting walks down
# creating nodes as needed; searching walks down
# and checks the flag; a prefix check only needs
# the walk to succeed.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
        node.is_word = True

    def search(self, word: str) -> bool:
        node = self._find(word)
        return node is not None and node.is_word

    def startsWith(self, prefix: str) -> bool:
        return self._find(prefix) is not None

    def _find(self, text: str):
        node = self.root
        for ch in text:
            node = node.children.get(ch)
            if node is None:
                return None
        return node
