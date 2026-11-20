class Solution {
    public List<Integer> busiestServers(int k, int[] arrival, int[] load) {
        // My thinking: each request wants its turn's server or
        // the next free one clockwise — so keep the free servers
        // sorted and the busy ones in a heap by finish time.
        java.util.TreeSet<Integer> free = new java.util.TreeSet<>();
        for (int i = 0; i < k; i++) free.add(i);
        java.util.PriorityQueue<int[]> busy = new java.util.PriorityQueue<>((a, b) -> a[0] - b[0]);
        int[] handled = new int[k];
        for (int i = 0; i < arrival.length; i++) {
            int t = arrival[i];
            while (!busy.isEmpty() && busy.peek()[0] <= t) {
                free.add(busy.poll()[1]);
            }
            if (free.isEmpty()) continue;
            int want = i % k;
            Integer sid = free.ceiling(want);
            if (sid == null) sid = free.first();
            free.remove(sid);
            handled[sid]++;
            busy.offer(new int[]{t + load[i], sid});
        }
        int most = 0;
        for (int c : handled) most = Math.max(most, c);
        java.util.List<Integer> out = new java.util.ArrayList<>();
        for (int i = 0; i < k; i++) if (handled[i] == most) out.add(i);
        return out;
    }
}
