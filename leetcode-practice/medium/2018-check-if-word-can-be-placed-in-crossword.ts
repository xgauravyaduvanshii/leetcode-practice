// LeetCode 2018. Check if Word Can Be Placed In Crossword — Medium
// https://leetcode.com/problems/check-if-word-can-be-placed-in-crossword/
// Submission 2204146276 — Accepted, TypeScript

// My thinking: a word can only sit in a stretch of open cells that is
// exactly as long as the word, with a '#' or the board edge on both
// sides. So I scan every row and every column, cut them into stretches
// separated by '#', and keep only the stretches whose length matches
// the word. A stretch fits if every cell is either blank or already
// holds the matching letter of the word, and I try the word both
// forwards and backwards, which covers placing it left-to-right,
// right-to-left, top-to-bottom and bottom-to-top in one go.
function placeWordInCrossword(board: string[][], word: string): boolean {
    const fits = (segment: string[], letters: string[]): boolean => {
        if (segment.length !== letters.length) return false;
        for (let i = 0; i < segment.length; i++) {
            if (segment[i] !== ' ' && segment[i] !== letters[i]) return false;
        }
        return true;
    };

    const forward = word.split('');
    const backward = [...forward].reverse();
    const m = board.length;
    const n = board[0].length;

    for (const row of board) {
        let start = 0;
        for (let j = 0; j <= n; j++) {
            if (j === n || row[j] === '#') {
                const segment = row.slice(start, j);
                if (fits(segment, forward) || fits(segment, backward)) return true;
                start = j + 1;
            }
        }
    }

    for (let j = 0; j < n; j++) {
        let start = 0;
        for (let i = 0; i <= m; i++) {
            if (i === m || board[i][j] === '#') {
                const segment: string[] = [];
                for (let k = start; k < i; k++) segment.push(board[k][j]);
                if (fits(segment, forward) || fits(segment, backward)) return true;
                start = i + 1;
            }
        }
    }

    return false;
}
