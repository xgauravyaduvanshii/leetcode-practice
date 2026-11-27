// LeetCode 79. Word Search — Medium
// https://leetcode.com/problems/word-search/
// Submission 2203849519 — Accepted, JavaScript

// My thinking: I try every cell as a starting point and search
// depth-first, marking each cell used while I am on it and unmarking
// it when I backtrack, so no cell is reused in one word. Before
// searching I flip the word when its last letter is rarer on the board
// than its first, which prunes the slow case where the search starts
// from a very common letter.
/**
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 */
var exist = function(board, word) {
    const counts = {};
    for (const row of board) {
        for (const ch of row) counts[ch] = (counts[ch] || 0) + 1;
    }
    if ((counts[word[0]] || 0) > (counts[word[word.length - 1]] || 0)) {
        word = word.split('').reverse().join('');
    }
    const m = board.length, n = board[0].length;

    function dfs(r, c, k) {
        if (k === word.length) return true;
        if (r < 0 || r >= m || c < 0 || c >= n) return false;
        if (board[r][c] !== word[k]) return false;
        const saved = board[r][c];
        board[r][c] = '#';
        const found = dfs(r + 1, c, k + 1) || dfs(r - 1, c, k + 1) ||
                      dfs(r, c + 1, k + 1) || dfs(r, c - 1, k + 1);
        board[r][c] = saved;
        return found;
    }

    for (let r = 0; r < m; r++) {
        for (let c = 0; c < n; c++) {
            if (board[r][c] === word[0] && dfs(r, c, 0)) return true;
        }
    }
    return false;
};
