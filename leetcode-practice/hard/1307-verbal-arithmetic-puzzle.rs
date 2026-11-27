use std::collections::HashMap;
use std::collections::HashSet;

impl Solution {
    pub fn is_solvable(words: Vec<String>, result: String) -> bool {
        // My thinking: give each letter a weight from the column
        // it sits in, then try the letters heaviest first — and
        // a one-letter word may be zero, since a lone 0 is not
        // a leading zero.
        let mut weight: HashMap<char, i64> = HashMap::new();
        for word in &words {
            for (i, ch) in word.chars().rev().enumerate() {
                *weight.entry(ch).or_insert(0) += 10i64.pow(i as u32);
            }
        }
        for (i, ch) in result.chars().rev().enumerate() {
            *weight.entry(ch).or_insert(0) -= 10i64.pow(i as u32);
        }
        let mut letters: Vec<char> = weight.keys().cloned().collect();
        letters.sort_by_key(|ch| -weight[ch].abs());
        let mut leading: HashSet<char> = HashSet::new();
        for word in &words {
            if word.len() > 1 {
                leading.insert(word.chars().next().unwrap());
            }
        }
        if result.len() > 1 {
            leading.insert(result.chars().next().unwrap());
        }
        let mut used = [false; 10];
        fn dfs(
            i: usize,
            total: i64,
            letters: &Vec<char>,
            weight: &HashMap<char, i64>,
            leading: &HashSet<char>,
            used: &mut [bool; 10],
        ) -> bool {
            if i == letters.len() {
                return total == 0;
            }
            let ch = letters[i];
            for d in 0..10 {
                if used[d] {
                    continue;
                }
                if d == 0 && leading.contains(&ch) {
                    continue;
                }
                used[d] = true;
                if dfs(i + 1, total + weight[&ch] * d as i64, letters, weight, leading, used) {
                    return true;
                }
                used[d] = false;
            }
            false
        }
        dfs(0, 0, &letters, &weight, &leading, &mut used)
    }
}
