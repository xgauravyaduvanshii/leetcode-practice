using System;

public class Solution {
    public double GetMinDistSum(int[][] positions) {
        // My thinking: the best spot pulls toward every point
        // at once — so start at the middle and keep sliding
        // toward the weighted centre until it stops moving.
        double x = 0, y = 0;
        foreach (var p in positions) { x += p[0]; y += p[1]; }
        x /= positions.Length;
        y /= positions.Length;
        for (int iter = 0; iter < 100; iter++) {
            double numX = 0, numY = 0, den = 0;
            foreach (var p in positions) {
                double d = Math.Sqrt((p[0] - x) * (p[0] - x) + (p[1] - y) * (p[1] - y));
                if (d < 1e-9) continue;
                numX += p[0] / d;
                numY += p[1] / d;
                den += 1 / d;
            }
            if (den == 0) break;
            double newX = numX / den, newY = numY / den;
            if (Math.Sqrt((newX - x) * (newX - x) + (newY - y) * (newY - y)) < 1e-7) {
                x = newX; y = newY;
                break;
            }
            x = newX; y = newY;
        }
        double total = 0;
        foreach (var p in positions) {
            total += Math.Sqrt((p[0] - x) * (p[0] - x) + (p[1] - y) * (p[1] - y));
        }
        return total;
    }
}
