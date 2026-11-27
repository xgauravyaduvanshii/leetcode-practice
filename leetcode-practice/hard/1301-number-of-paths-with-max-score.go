func pathsWithMaxScore(board []string) []int {
	// My thinking: walk backwards from S to E, keeping the
	// best score and how many ways reach it — and track
	// reachability by score, since a count of 0 modulo
	// 1e9+7 does not mean the cell is unreachable.
	const MOD = 1000000007
	const NEG = -1000000000
	n := len(board)
	score := make([][]int, n)
	count := make([][]int, n)
	for i := range score {
		score[i] = make([]int, n)
		count[i] = make([]int, n)
		for j := range score[i] {
			score[i][j] = NEG
		}
	}
	score[n-1][n-1] = 0
	count[n-1][n-1] = 1
	for r := n - 1; r >= 0; r-- {
		for c := n - 1; c >= 0; c-- {
			if board[r][c] == 'X' {
				continue
			}
			if r == n-1 && c == n-1 {
				continue
			}
			best := NEG
			ways := 0
			for _, d := range [][2]int{{1, 0}, {0, 1}, {1, 1}} {
				nr, nc := r+d[0], c+d[1]
				if nr < n && nc < n && score[nr][nc] != NEG {
					if score[nr][nc] > best {
						best = score[nr][nc]
						ways = count[nr][nc]
					} else if score[nr][nc] == best {
						ways = (ways + count[nr][nc]) % MOD
					}
				}
			}
			if best == NEG {
				continue
			}
			add := 0
			if board[r][c] >= '1' && board[r][c] <= '9' {
				add = int(board[r][c] - '0')
			}
			score[r][c] = best + add
			count[r][c] = ways
		}
	}
	if score[0][0] == NEG {
		return []int{0, 0}
	}
	return []int{score[0][0], count[0][0]}
}
