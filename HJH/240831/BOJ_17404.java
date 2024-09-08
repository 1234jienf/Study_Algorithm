package 자율팀스터디.d240831;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ_17404 {
	static int n, nM1;
	static int[][] dp; // 첫 번째 인덱스가 n
	static int[][] dists;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		n = Integer.parseInt(br.readLine());
		nM1 = n-1;

		dists = new int[n][3];
		int r, g, b;
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			r = Integer.parseInt(st.nextToken());
			g = Integer.parseInt(st.nextToken());
			b = Integer.parseInt(st.nextToken());
			dists[i][0] = r;
			dists[i][1] = g;
			dists[i][2] = b;
		}

		dp = new int[n][3];
		for (int i = 0; i < n; i++) {
			Arrays.fill(dp[i], Integer.MAX_VALUE / 2);
		}
		// 0 번째가 r
		dp[0][0] = dists[0][0];
		for (int i = 1; i < nM1; i++) {
			dp[i][0] = Math.min(dp[i][0], dp[i-1][1] + dists[i][0]);
			dp[i][0] = Math.min(dp[i][0], dp[i-1][2] + dists[i][0]);

			dp[i][1] = Math.min(dp[i][1], dp[i-1][0] + dists[i][1]);
			dp[i][1] = Math.min(dp[i][1], dp[i-1][2] + dists[i][1]);

			dp[i][2] = Math.min(dp[i][2], dp[i-1][0] + dists[i][2]);
			dp[i][2] = Math.min(dp[i][2], dp[i-1][1] + dists[i][2]);
		}
		dp[nM1][1] = Math.min(dp[nM1][1], dp[nM1-1][0] + dists[nM1][1]);
		dp[nM1][1] = Math.min(dp[nM1][1], dp[nM1-1][2] + dists[nM1][1]);

		dp[nM1][2] = Math.min(dp[nM1][2], dp[nM1-1][0] + dists[nM1][2]);
		dp[nM1][2] = Math.min(dp[nM1][2], dp[nM1-1][1] + dists[nM1][2]);
		int ans = Math.min(Math.min(dp[nM1][0], dp[nM1][1]),dp[nM1][2]);

		//===================
		dp = new int[n][3];
		for (int i = 0; i < n; i++) {
			Arrays.fill(dp[i], Integer.MAX_VALUE / 2);
		}
		// 0 번째가 g
		dp[0][0] = Integer.MAX_VALUE / 2;
		dp[0][1] = dists[0][1];
		for (int i = 1; i < nM1; i++) {
			dp[i][0] = Math.min(dp[i][0], dp[i-1][1] + dists[i][0]);
			dp[i][0] = Math.min(dp[i][0], dp[i-1][2] + dists[i][0]);

			dp[i][1] = Math.min(dp[i][1], dp[i-1][0] + dists[i][1]);
			dp[i][1] = Math.min(dp[i][1], dp[i-1][2] + dists[i][1]);

			dp[i][2] = Math.min(dp[i][2], dp[i-1][0] + dists[i][2]);
			dp[i][2] = Math.min(dp[i][2], dp[i-1][1] + dists[i][2]);
		}
		dp[nM1][0] = Math.min(dp[nM1][0], dp[nM1-1][1] + dists[nM1][0]);
		dp[nM1][0] = Math.min(dp[nM1][0], dp[nM1-1][2] + dists[nM1][0]);

		dp[nM1][2] = Math.min(dp[nM1][2], dp[nM1-1][0] + dists[nM1][2]);
		dp[nM1][2] = Math.min(dp[nM1][2], dp[nM1-1][1] + dists[nM1][2]);
		ans = Math.min(Math.min(Math.min(dp[nM1][0], dp[nM1][1]),dp[nM1][2]), ans);

		//===================
		dp = new int[n][3];
		for (int i = 0; i < n; i++) {
			Arrays.fill(dp[i], Integer.MAX_VALUE / 2);
		}
		// 0 번째가 g
		// 0 번째가 b
		dp[0][1] = Integer.MAX_VALUE / 2;
		dp[0][2] = dists[0][2];
		for (int i = 1; i < nM1; i++) {
			dp[i][0] = Math.min(dp[i][0], dp[i-1][1] + dists[i][0]);
			dp[i][0] = Math.min(dp[i][0], dp[i-1][2] + dists[i][0]);

			dp[i][1] = Math.min(dp[i][1], dp[i-1][0] + dists[i][1]);
			dp[i][1] = Math.min(dp[i][1], dp[i-1][2] + dists[i][1]);

			dp[i][2] = Math.min(dp[i][2], dp[i-1][0] + dists[i][2]);
			dp[i][2] = Math.min(dp[i][2], dp[i-1][1] + dists[i][2]);
		}
		dp[nM1][0] = Math.min(dp[nM1][0], dp[nM1-1][1] + dists[nM1][0]);
		dp[nM1][0] = Math.min(dp[nM1][0], dp[nM1-1][2] + dists[nM1][0]);

		dp[nM1][1] = Math.min(dp[nM1][1], dp[nM1-1][0] + dists[nM1][1]);
		dp[nM1][1] = Math.min(dp[nM1][1], dp[nM1-1][2] + dists[nM1][1]);
		ans = Math.min(Math.min(Math.min(dp[nM1][0], dp[nM1][1]),dp[nM1][2]), ans);

		System.out.println(ans);
	}
}