package 자율팀스터디.d240908;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ_2458 {
	static int n, m;
	static int[][] fw;
	static int INF = Integer.MAX_VALUE / 2;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());

		fw = new int[n+1][n+1];
		for (int i = 0; i <= n; i++) {
			Arrays.fill(fw[i], INF);
			fw[i][i] = 0;
		}

		int a, b;
		for (int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			a = Integer.parseInt(st.nextToken());
			b = Integer.parseInt(st.nextToken());
			fw[a][b] = 1;
		}

		for (int via = 1; via <= n; via++) {
			for (a = 1; a <= n; a++) {
				for (b = 1; b <= n; b++) {
					fw[a][b] = Math.min(fw[a][b], fw[a][via] + fw[via][b]);
				}
			}
		}

		int cnt = 0;
		for (int i = 1; i <= n; i++) {
			if (isOrderFixed(i))
				cnt++;
		}
		System.out.println(cnt);
	}

	private static boolean isOrderFixed(int node) {
		for (int i = 1; i <= n; i++) {
			if (fw[i][node] == INF && fw[node][i] == INF)
				return false;
		}
		return true;
	}
}