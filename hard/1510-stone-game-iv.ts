function winnerSquareGame(n: number): boolean {
    // My thinking: with i stones, you win if any square
    // you take leaves the other player a losing pile —
    // so work upward from zero and mark each pile.
    const dp: boolean[] = new Array(n + 1).fill(false);
    for (let i = 1; i <= n; i++) {
        for (let j = 1; j * j <= i; j++) {
            if (!dp[i - j * j]) {
                dp[i] = true;
                break;
            }
        }
    }
    return dp[n];
}
