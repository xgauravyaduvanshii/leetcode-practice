// LeetCode 1948. Delete Duplicate Folders in System — Hard
// https://leetcode.com/problems/delete-duplicate-folders-in-system/
// Submission 2201263483 — Accepted, Go
//
// My thinking: I build a trie of the folders and
// fingerprint each subtree by its children's names
// and fingerprints — a folder whose fingerprint
// shows up twice is a duplicate and goes, whole
// subtree included. An empty folder has no
// fingerprint to match, so it stays.

import "sort"

type folderNode struct {
	children map[string]*folderNode
	serial   string
}

func deleteDuplicateFolder(paths [][]string) [][]string {
	root := &folderNode{children: make(map[string]*folderNode)}
	for _, path := range paths {
		node := root
		for _, name := range path {
			child, ok := node.children[name]
			if !ok {
				child = &folderNode{children: make(map[string]*folderNode)}
				node.children[name] = child
			}
			node = child
		}
	}
	count := make(map[string]int)
	var serialize func(node *folderNode) string
	serialize = func(node *folderNode) string {
		if len(node.children) == 0 {
			return ""
		}
		names := make([]string, 0, len(node.children))
		for name := range node.children {
			names = append(names, name)
		}
		sort.Strings(names)
		s := ""
		for i, name := range names {
			if i > 0 {
				s += ","
			}
			s += name + "(" + serialize(node.children[name]) + ")"
		}
		node.serial = s
		count[s]++
		return s
	}
	serialize(root)
	var ans [][]string
	var dfs func(node *folderNode, path []string)
	dfs = func(node *folderNode, path []string) {
		names := make([]string, 0, len(node.children))
		for name := range node.children {
			names = append(names, name)
		}
		sort.Strings(names)
		for _, name := range names {
			child := node.children[name]
			if count[child.serial] > 1 {
				continue
			}
			next := append(append([]string{}, path...), name)
			ans = append(ans, next)
			dfs(child, next)
		}
	}
	dfs(root, []string{})
	return ans
}
