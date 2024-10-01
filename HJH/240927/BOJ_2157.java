package 자율팀스터디.d240928;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ_2157 {
	static int n, m, k;
	static List<Node>[] graph;
	static int[][] dp;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		k = Integer.parseInt(st.nextToken());

		graph = new ArrayList[n+1];
		for (int i = 0; i <= n; i++) graph[i] = new ArrayList<>();

		int[][] bests = new int[n+1][n+1];
		int a, b, c;
		for (int i = 0; i < k; i++) {
			st = new StringTokenizer(br.readLine());
			a = Integer.parseInt(st.nextToken());
			b = Integer.parseInt(st.nextToken());
			c = Integer.parseInt(st.nextToken());

			if (b < a) continue;
			bests[a][b] = Math.max(bests[a][b], c);
		}
		for (int i = 1; i <= n; i++)
			for (int j = i; j <= n; j++)
				if (bests[i][j] != 0)
					graph[i].add(new Node(j, bests[i][j]));

		// i번 + 1번을 통해 갈 수 있는 위치들을 계산
		dp = new int[n+1][m+1];
		for (int i = 0; i <= n; i++)
			Arrays.fill(dp[i], Integer.MIN_VALUE);
		dp[1][1] = 0;
		Queue<Node> q = new ArrayDeque<>();
		q.add(new Node(1, 0));
		for (int i = 1; i < m; i++) {
			for (int node = 1; node <= n; node++) {
				for (Node next : graph[node]) {
					dp[next.v][i+1] = Math.max(dp[next.v][i+1], dp[node][i] + next.e);
				}
			}
		}
		int ans = 0;
		for (int i = 0; i <= m; i++) {
			ans = Math.max(ans, dp[n][i]);
		}
		System.out.println(ans);
	}

	static class Node {
		int v, e;

		public Node(int v, int e) {
			this.v = v;
			this.e = e;
		}
	}
}