import java.io.*;
import java.util.*;

public class Main {

    static int n, s;
    static int[] arr;
    static int[] sums;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        s = Integer.parseInt(st.nextToken());

        arr = new int[n];
        sums = new int[n+1];
        sums[0] = 0;
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
            sums[i+1] = sums[i] + arr[i];
        }

        int l = 0;
        int r = 1;
        int ans = Integer.MAX_VALUE;
        while (true) {
            int sum = sums[r] - sums[l];
            if (sum >= s) {
                ans = Math.min(ans, r-l);
                l++;
            }
            else {
                r++;
            }
            if (r == n + 1)
                break;
        }
        System.out.println(ans== Integer.MAX_VALUE?0:ans);

    }
}