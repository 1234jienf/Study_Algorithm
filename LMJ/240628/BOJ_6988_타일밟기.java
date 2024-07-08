import java.io.*;
import java.util.*;

public class BOJ_6988_타일밟기 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int n = Integer.parseInt(br.readLine());
        int[] a = new int[n];
        int[] pos = new int[1000001]; // 1000001까지의 인덱스 사용
        Arrays.fill(pos, -1); // -1로 초기화
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            a[i] = Integer.parseInt(st.nextToken());
            pos[a[i]] = i;
        }
        
        long[][] d = new long[n][n];
        long ans = 0;

        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int bb = -1;
                if (2 * a[i] - a[j] >= 0) {
                    bb = pos[2 * a[i] - a[j]];
                }
                if (bb == -1) {
                    d[i][j] = a[i] + a[j];
                } else {
                    d[i][j] = d[bb][i] + a[j];
                }
                if (d[i][j] > ans && bb != -1) {
                    ans = d[i][j];
                }
            }
        }
        System.out.println(ans);
    }
}
