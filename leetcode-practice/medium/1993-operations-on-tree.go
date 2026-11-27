// LeetCode 1993. Operations on Tree — Medium
// https://leetcode.com/problems/operations-on-tree/
// Submission 2204113020 — Accepted, Go

// My thinking: keep each node's locker (0 means unlocked, users are
// positive) plus a children list built from the parent array. lock()
// needs the node free, no locked ancestor (walk up the parent chain)
// and no locked descendant (walk down the children). unlock() only
// succeeds for the user who locked the node. upgrade() needs the node
// free, at least one locked descendant and no locked ancestor, then
// it frees every locked descendant and locks the node itself.
type LockingTree struct {
    parent   []int
    locked   []int
    children [][]int
}

func Constructor(parent []int) LockingTree {
    tree := LockingTree{
        parent:   parent,
        locked:   make([]int, len(parent)),
        children: make([][]int, len(parent)),
    }
    for i, p := range parent {
        if p != -1 {
            tree.children[p] = append(tree.children[p], i)
        }
    }
    return tree
}

func (this *LockingTree) hasLockedAncestor(num int) bool {
    for p := this.parent[num]; p != -1; p = this.parent[p] {
        if this.locked[p] != 0 {
            return true
        }
    }
    return false
}

func (this *LockingTree) lockedDescendants(num int) []int {
    var found []int
    stack := append([]int(nil), this.children[num]...)
    for len(stack) > 0 {
        node := stack[len(stack)-1]
        stack = stack[:len(stack)-1]
        if this.locked[node] != 0 {
            found = append(found, node)
        }
        stack = append(stack, this.children[node]...)
    }
    return found
}

func (this *LockingTree) Lock(num int, user int) bool {
    if this.locked[num] != 0 {
        return false
    }
    if this.hasLockedAncestor(num) {
        return false
    }
    if len(this.lockedDescendants(num)) > 0 {
        return false
    }
    this.locked[num] = user
    return true
}

func (this *LockingTree) Unlock(num int, user int) bool {
    if this.locked[num] != user {
        return false
    }
    this.locked[num] = 0
    return true
}

func (this *LockingTree) Upgrade(num int, user int) bool {
    if this.locked[num] != 0 {
        return false
    }
    if this.hasLockedAncestor(num) {
        return false
    }
    desc := this.lockedDescendants(num)
    if len(desc) == 0 {
        return false
    }
    for _, node := range desc {
        this.locked[node] = 0
    }
    this.locked[num] = user
    return true
}
