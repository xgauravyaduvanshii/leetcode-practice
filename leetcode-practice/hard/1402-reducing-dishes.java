import java.util.Arrays;

class Solution {
    public int maxSatisfaction(int[] satisfaction) {
        // My thinking: cook the best dishes last — sort them,
        // then keep adding the next dish while the dishes
        // already chosen still earn more than they cost.
        Arrays.sort(satisfaction);
        int total = 0, suffix = 0;
        for (int i = satisfaction.length - 1; i >= 0; i--) {
            suffix += satisfaction[i];
            if (suffix <= 0) break;
            total += suffix;
        }
        return total;
    }
}
