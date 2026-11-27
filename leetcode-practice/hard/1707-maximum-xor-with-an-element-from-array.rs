// LeetCode 1707. Maximum XOR With an Element From Array — Hard
// https://leetcode.com/problems/maximum-xor-with-an-element-from-array/
// Submission 2201106719 — Accepted, Rust
//
// My thinking: I sort the numbers and the queries by
// their limits, then grow a binary trie with every
// number the current limit allows — each query is then
// answered by walking the trie down the opposite bit
// at every step to maximise the xor.

#[derive(Default)]
struct TrieNode {
    child: [Option<Box<TrieNode>>; 2],
}

impl TrieNode {
    fn insert(&mut self, num: i32) {
        let mut node = self;
        for bit in (0..=30).rev() {
            let b = ((num >> bit) & 1) as usize;
            node = node.child[b].get_or_insert_with(Default::default);
        }
    }

    fn best_xor(&self, num: i32) -> i32 {
        let mut node = self;
        let mut result = 0;
        for bit in (0..=30).rev() {
            let b = ((num >> bit) & 1) as usize;
            if node.child[1 - b].is_some() {
                result |= 1 << bit;
                node = node.child[1 - b].as_ref().unwrap();
            } else {
                node = node.child[b].as_ref().unwrap();
            }
        }
        result
    }
}

impl Solution {
    pub fn maximize_xor(mut nums: Vec<i32>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        nums.sort_unstable();
        let mut order: Vec<usize> = (0..queries.len()).collect();
        order.sort_by_key(|&i| queries[i][1]);
        let mut trie = TrieNode::default();
        let mut inserted = 0usize;
        let mut answer = vec![0; queries.len()];
        for &i in &order {
            let (xi, mi) = (queries[i][0], queries[i][1]);
            while inserted < nums.len() && nums[inserted] <= mi {
                trie.insert(nums[inserted]);
                inserted += 1;
            }
            answer[i] = if inserted == 0 { -1 } else { trie.best_xor(xi) };
        }
        answer
    }
}
