// LeetCode 130. Surrounded Regions — Medium
// https://leetcode.com/problems/surrounded-regions/
// Submission 2204028567 — Accepted, JavaScript
//
// My thinking: an 'O' region is only safe when it touches the border,
// so I start a depth-first search from every border 'O' and mark the
// whole connected region as safe with a temporary marker. Any 'O' that
// is left unmarked is fully surrounded, so I flip it to 'X', and then
// I turn the temporary markers back into 'O'. The board is changed in
// place, so the extra memory is just the recursion stack.

/**
 * @param {character[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 */
var solve = function(board) {
    if (!board.length || !board[0].length) return;
    const m = board.length;
    const n = board[0].length;

    const dfs = (r, c) => {
        if (r < 0 || r >= m || c < 0 || c >= n) return;
        if (board[r][c] !== 'O') return;
        board[r][c] = '#';
        dfs(r + 1, c);
        dfs(r - 1, c);
        dfs(r, c + 1);
        dfs(r, c - 1);
    };

    for (let r = 0; r < m; r++) {
        dfs(r, 0);
        dfs(r, n - 1);
    }
    for (let c = 0; c < n; c++) {
        dfs(0, c);
        dfs(m - 1, c);
    }

    for (let r = 0; r < m; r++) {
        for (let c = 0; c < n; c++) {
            if (board[r][c] === 'O') board[r][c] = 'X';
            else if (board[r][c] === '#') board[r][c] = 'O';
        }
    }
};
