import java.util.Arrays;

class Solution {
    public String largestMultipleOfThree(int[] digits) {
        // My thinking: the biggest number is the digits in
        // descending order — just drop the smallest digits
        // that fix the remainder when the sum is not a
        // multiple of three.
        Arrays.sort(digits);
        int total = 0;
        for (int d : digits) total += d;
        boolean[] removed = new boolean[digits.length];
        if (total % 3 == 1) {
            if (!drop(digits, removed, 1, 1) && !drop(digits, removed, 2, 2)) return "";
        } else if (total % 3 == 2) {
            if (!drop(digits, removed, 2, 1) && !drop(digits, removed, 1, 2)) return "";
        }
        StringBuilder sb = new StringBuilder();
        for (int i = digits.length - 1; i >= 0; i--) {
            if (!removed[i]) sb.append(digits[i]);
        }
        if (sb.length() == 0) return "";
        if (sb.charAt(0) == '0') return "0";
        return sb.toString();
    }

    private boolean drop(int[] digits, boolean[] removed, int residue, int k) {
        int available = 0;
        for (int i = 0; i < digits.length; i++) {
            if (!removed[i] && digits[i] % 3 == residue) available++;
        }
        if (available < k) return false;
        int count = 0;
        for (int i = 0; i < digits.length && count < k; i++) {
            if (!removed[i] && digits[i] % 3 == residue) {
                removed[i] = true;
                count++;
            }
        }
        return true;
    }
}
