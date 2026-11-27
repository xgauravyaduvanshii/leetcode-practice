// LeetCode 2353. Design a Food Rating System — Medium
// https://leetcode.com/problems/design-a-food-rating-system/
// Submission 2204735108 — Accepted, Rust
//
// My thinking: same idea as the Python version — a food->(cuisine,
// rating) map plus one max-heap per cuisine, ordered by rating then by
// the reverse of the food name so ties break to the lexicographically
// smallest name. Ratings are pushed fresh on change; highestRated lazily
// pops stale tops. The methods take &mut self, as the template allows.
use std::cmp::Ordering;
use std::collections::{BinaryHeap, HashMap};

#[derive(Eq, PartialEq)]
struct Entry {
    rating: i32,
    food: String,
}

impl Ord for Entry {
    fn cmp(&self, other: &Self) -> Ordering {
        self.rating.cmp(&other.rating).then_with(|| other.food.cmp(&self.food))
    }
}

impl PartialOrd for Entry {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

struct FoodRatings {
    food_info: HashMap<String, (String, i32)>,
    cuisine_heap: HashMap<String, BinaryHeap<Entry>>,
}

impl FoodRatings {
    fn new(foods: Vec<String>, cuisines: Vec<String>, ratings: Vec<i32>) -> Self {
        let mut food_info = HashMap::new();
        let mut cuisine_heap: HashMap<String, BinaryHeap<Entry>> = HashMap::new();
        for i in 0..foods.len() {
            food_info.insert(foods[i].clone(), (cuisines[i].clone(), ratings[i]));
            cuisine_heap.entry(cuisines[i].clone()).or_default().push(Entry { rating: ratings[i], food: foods[i].clone() });
        }
        FoodRatings { food_info, cuisine_heap }
    }

    fn change_rating(&mut self, food: String, new_rating: i32) {
        let (cuisine, _) = self.food_info.get(&food).unwrap().clone();
        self.food_info.insert(food.clone(), (cuisine.clone(), new_rating));
        self.cuisine_heap.entry(cuisine).or_default().push(Entry { rating: new_rating, food });
    }

    fn highest_rated(&mut self, cuisine: String) -> String {
        let heap = self.cuisine_heap.get_mut(&cuisine).unwrap();
        loop {
            let top = heap.peek().unwrap();
            let cur = self.food_info.get(&top.food).unwrap().1;
            if cur == top.rating {
                return top.food.clone();
            }
            heap.pop();
        }
    }
}
