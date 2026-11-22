# LeetCode 1948. Delete Duplicate Folders in System — Hard
# https://leetcode.com/problems/delete-duplicate-folders-in-system/
# Submission 2201258029 — Accepted, Python3
#
# My thinking: I build a trie of the folders and
# fingerprint each subtree by its children's names
# and fingerprints — a folder whose fingerprint
# shows up twice is a duplicate and goes, whole
# subtree included. An empty folder has no
# fingerprint to match, so it stays.

class Solution:
    def deleteDuplicateFolder(self, paths: list[list[str]]) -> list[list[str]]:
        trie = {}
        for path in paths:
            node = trie
            for name in path:
                node = node.setdefault(name, {})
        serial_of = {}
        count = {}

        def serialize(node):
            if not node:
                return ""
            parts = []
            for name in sorted(node):
                parts.append(name + "(" + serialize(node[name]) + ")")
            s = ",".join(parts)
            serial_of[id(node)] = s
            count[s] = count.get(s, 0) + 1
            return s

        serialize(trie)
        ans = []

        def dfs(node, path):
            for name in sorted(node):
                child = node[name]
                if count[serial_of[id(child)]] > 1:
                    continue
                ans.append(path + [name])
                dfs(child, path + [name])

        dfs(trie, [])
        return ans
