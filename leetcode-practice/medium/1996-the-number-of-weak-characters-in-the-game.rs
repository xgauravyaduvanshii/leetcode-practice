// LeetCode 1996. The Number of Weak Characters in the Game — Medium
// https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/
// Submission 2204116700 — Accepted, Rust

// My thinking: A character is weak only if some other character beats
// it on both attack and defense, so I sort by attack from highest to
// lowest. Characters with the same attack can never make each other
// weak, so inside one attack group I sort defense from lowest to
// highest. Then I walk the sorted list keeping the best defense I have
// seen so far, which always comes from a strictly higher attack. If the
// current character's defense is below that best defense, a stronger
// character exists on both counts and it is weak. Otherwise I update
// the best defense with this character's defense and move on.
impl Solution {
    pub fn number_of_weak_characters(mut properties: Vec<Vec<i32>>) -> i32 {
        properties.sort_by(|a, b| b[0].cmp(&a[0]).then(a[1].cmp(&b[1])));
        let mut weak = 0;
        let mut max_defense = 0;
        for p in &properties {
            if p[1] < max_defense {
                weak += 1;
            } else {
                max_defense = p[1];
            }
        }
        weak
    }
}
