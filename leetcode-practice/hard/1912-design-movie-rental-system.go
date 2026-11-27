// LeetCode 1912. Design Movie Rental System — Hard
// https://leetcode.com/problems/design-movie-rental-system/
// Submission 2201230260 — Accepted, Go
//
// My thinking: unrented copies sit in a heap per
// movie ordered by price then shop, rented copies
// in one heap ordered by price then shop then
// movie — a rented set tells me which heap entries
// have gone stale, so I skip them lazily.

import "container/heap"

type priceShop struct {
	price int
	shop  int
}

type priceShopHeap []priceShop

func (h priceShopHeap) Len() int { return len(h) }
func (h priceShopHeap) Less(i, j int) bool {
	if h[i].price != h[j].price {
		return h[i].price < h[j].price
	}
	return h[i].shop < h[j].shop
}
func (h priceShopHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *priceShopHeap) Push(x interface{}) { *h = append(*h, x.(priceShop)) }
func (h *priceShopHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

type priceShopMovie struct {
	price int
	shop  int
	movie int
}

type priceShopMovieHeap []priceShopMovie

func (h priceShopMovieHeap) Len() int { return len(h) }
func (h priceShopMovieHeap) Less(i, j int) bool {
	if h[i].price != h[j].price {
		return h[i].price < h[j].price
	}
	if h[i].shop != h[j].shop {
		return h[i].shop < h[j].shop
	}
	return h[i].movie < h[j].movie
}
func (h priceShopMovieHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *priceShopMovieHeap) Push(x interface{}) { *h = append(*h, x.(priceShopMovie)) }
func (h *priceShopMovieHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

type shopMovie struct {
	shop  int
	movie int
}

type MovieRentingSystem struct {
	prices    map[shopMovie]int
	unrented  map[int]*priceShopHeap
	rented    *priceShopMovieHeap
	rentedSet map[shopMovie]bool
}

func Constructor(n int, entries [][]int) MovieRentingSystem {
	s := MovieRentingSystem{
		prices:    make(map[shopMovie]int),
		unrented:  make(map[int]*priceShopHeap),
		rented:    &priceShopMovieHeap{},
		rentedSet: make(map[shopMovie]bool),
	}
	for _, e := range entries {
		shop, movie, price := e[0], e[1], e[2]
		s.prices[shopMovie{shop, movie}] = price
		h, ok := s.unrented[movie]
		if !ok {
			h = &priceShopHeap{}
			s.unrented[movie] = h
		}
		*h = append(*h, priceShop{price, shop})
	}
	for _, h := range s.unrented {
		heap.Init(h)
	}
	heap.Init(s.rented)
	return s
}

func (s *MovieRentingSystem) Search(movie int) []int {
	h, ok := s.unrented[movie]
	if !ok {
		return []int{}
	}
	res := []int{}
	tmp := []priceShop{}
	for h.Len() > 0 && len(res) < 5 {
		top := heap.Pop(h).(priceShop)
		if !s.rentedSet[shopMovie{top.shop, movie}] {
			res = append(res, top.shop)
		}
		tmp = append(tmp, top)
	}
	for _, item := range tmp {
		heap.Push(h, item)
	}
	return res
}

func (s *MovieRentingSystem) Rent(shop int, movie int) {
	s.rentedSet[shopMovie{shop, movie}] = true
	heap.Push(s.rented, priceShopMovie{s.prices[shopMovie{shop, movie}], shop, movie})
}

func (s *MovieRentingSystem) Drop(shop int, movie int) {
	delete(s.rentedSet, shopMovie{shop, movie})
}

func (s *MovieRentingSystem) Report() [][]int {
	res := [][]int{}
	tmp := []priceShopMovie{}
	seen := make(map[shopMovie]bool)
	for s.rented.Len() > 0 && len(res) < 5 {
		top := heap.Pop(s.rented).(priceShopMovie)
		key := shopMovie{top.shop, top.movie}
		if !s.rentedSet[key] || seen[key] {
			continue
		}
		seen[key] = true
		res = append(res, []int{top.shop, top.movie})
		tmp = append(tmp, top)
	}
	for _, item := range tmp {
		heap.Push(s.rented, item)
	}
	return res
}
