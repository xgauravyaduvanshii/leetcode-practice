// LeetCode 1728. Cat and Mouse II — Hard
// https://leetcode.com/problems/cat-and-mouse-ii/
// Submission 2201121835 — Accepted, Java
//
// My thinking: I treat every mouse/cat/turn combination
// as a game state and work backwards from the states
// where someone has already won — a state is won for
// the mouse if the mouse can move to a won state, or
// if every cat move from it is won; states nobody
// claims are draws, and a draw is not a mouse win.

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.Queue;

class Solution {
    public boolean canMouseWin(String[] grid, int catJump, int mouseJump) {
        int rows = grid.length;
        int cols = grid[0].length();
        int n = rows * cols;
        int mouse = -1, cat = -1, food = -1;
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r].charAt(c) == 'M') mouse = r * cols + c;
                else if (grid[r].charAt(c) == 'C') cat = r * cols + c;
                else if (grid[r].charAt(c) == 'F') food = r * cols + c;
            }
        }
        List<List<Integer>> mouseMoves = new ArrayList<>();
        List<List<Integer>> catMoves = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            mouseMoves.add(moves(grid, rows, cols, i, mouseJump));
            catMoves.add(moves(grid, rows, cols, i, catJump));
        }
        // result[m][c][turn]: 0 unknown, 1 mouse wins, 2 cat wins
        int[][][] result = new int[n][n][2];
        int[][][] degree = new int[n][n][2];
        Queue<int[]> queue = new ArrayDeque<>();
        for (int m = 0; m < n; m++) {
            for (int c = 0; c < n; c++) {
                degree[m][c][0] = mouseMoves.get(m).size();
                degree[m][c][1] = catMoves.get(c).size();
                if (m == food) {
                    result[m][c][0] = result[m][c][1] = 1;
                    queue.offer(new int[]{m, c, 0});
                    queue.offer(new int[]{m, c, 1});
                } else if (c == food || m == c) {
                    result[m][c][0] = result[m][c][1] = 2;
                    queue.offer(new int[]{m, c, 0});
                    queue.offer(new int[]{m, c, 1});
                }
            }
        }
        while (!queue.isEmpty()) {
            int[] state = queue.poll();
            int m = state[0], c = state[1], turn = state[2];
            int outcome = result[m][c][turn];
            if (turn == 1) {
                for (int pm = 0; pm < n; pm++) {
                    if (result[pm][c][0] != 0 || !mouseMoves.get(pm).contains(m)) continue;
                    if (outcome == 1) {
                        result[pm][c][0] = 1;
                        queue.offer(new int[]{pm, c, 0});
                    } else if (--degree[pm][c][0] == 0) {
                        result[pm][c][0] = 2;
                        queue.offer(new int[]{pm, c, 0});
                    }
                }
            } else {
                for (int pc = 0; pc < n; pc++) {
                    if (result[m][pc][1] != 0 || !catMoves.get(pc).contains(c)) continue;
                    if (outcome == 2) {
                        result[m][pc][1] = 2;
                        queue.offer(new int[]{m, pc, 1});
                    } else if (--degree[m][pc][1] == 0) {
                        result[m][pc][1] = 1;
                        queue.offer(new int[]{m, pc, 1});
                    }
                }
            }
        }
        return result[mouse][cat][0] == 1;
    }

    private List<Integer> moves(String[] grid, int rows, int cols, int pos, int jump) {
        List<Integer> out = new ArrayList<>();
        out.add(pos);
        int r = pos / cols, c = pos % cols;
        int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        for (int[] d : dirs) {
            for (int step = 1; step <= jump; step++) {
                int nr = r + d[0] * step, nc = c + d[1] * step;
                if (nr < 0 || nr >= rows || nc < 0 || nc >= cols || grid[nr].charAt(nc) == '#') break;
                out.add(nr * cols + nc);
            }
        }
        return out;
    }
}
